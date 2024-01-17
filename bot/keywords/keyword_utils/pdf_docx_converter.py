import asyncio
import os

from typing import List, Tuple

from pdf2docx import Converter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from bot.config import bot
from bot.keywords.keyword_utils.image_to_file_converter import FileConverter, FileLoader


class DocumentLoader(FileLoader):
    async def save_files(self, file_ids: List[str], **kwargs) -> List[str]:
        file_extension = kwargs["file_extension"]
        document_list = await self._files_processing(
            file_ids, file_extension=file_extension
        )
        return document_list

    async def _files_processing(
        self, file_ids: List[str], file_extension: str = None
    ) -> List[str]:
        file_path_list = []

        for file_index, file_id in enumerate(file_ids):
            file_info = await bot.get_file(file_id)
            file_path = file_info.file_path
            file = await bot.download_file(file_path)

            filename = f"document_{file_index}.{file_extension}"
            temp_file_path = os.path.join(self.temp_dir, filename)
            with open(temp_file_path, "wb") as temp_file:
                temp_file.write(file.getvalue())

            file_path_list.append(temp_file_path)

        return file_path_list


class DocxToPdf(FileConverter):
    LOAD_TIMEOUT = 10

    async def convert(
        self, conversion_file_path: str, paths: List[str], **kwargs
    ) -> None:
        await self._parse_page(conversion_file_path, paths)

    async def _parse_page(self, conversion_file_path: str, paths: List[str]) -> None:
        docx_file = os.path.join(conversion_file_path)
        dir_name = paths[0]

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(
            "prefs",
            {
                "download.default_directory": dir_name,
            },
        )
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://smallpdf.com/word-to-pdf")

        upload_file_button_xpath = "//input[@type='file']"

        file_input = WebDriverWait(driver, self.LOAD_TIMEOUT).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, upload_file_button_xpath)
            )
        )
        file_input.send_keys(docx_file)

        download_file_button_xpath = "//div//span[contains(text(), 'Download')]"
        file_output = WebDriverWait(driver, self.LOAD_TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, download_file_button_xpath)
            )
        )
        file_output.click()
        await asyncio.sleep(self.LOAD_TIMEOUT)
        self.rename_pdf(docx_file)

    @staticmethod
    def rename_pdf(docx_file_path: str) -> None:
        pdf_file_path = os.path.splitext(docx_file_path)[0] + ".pdf"
        if os.path.exists(pdf_file_path):
            new_pdf_file_path = os.path.join(
                os.path.dirname(pdf_file_path), "result.pdf"
            )
            os.rename(pdf_file_path, new_pdf_file_path)

    def compress(
        self, image_file: str, compression_allowed: bool
    ) -> Tuple[str, int, int] | str:
        raise NotImplementedError


class PdfToDocx(FileConverter):
    def convert(self, conversion_file_path: str, paths: List[str], **kwargs) -> None:
        pdf_file = os.path.join(conversion_file_path)
        docx_file = os.path.join(paths[0], "result.docx")

        conversion_file = Converter(pdf_file)
        conversion_file.convert(docx_file)
        conversion_file.close()

    def compress(
        self, image_file: str, compression_allowed: bool
    ) -> Tuple[str, int, int] | str:
        raise NotImplementedError
