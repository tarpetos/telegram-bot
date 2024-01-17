from typing import Optional

from aiogram import types
from aiogram.types import InputFile
from aiogram.utils.exceptions import NetworkError

from bot.config import bot


async def is_document_sent(
    message: types.Message, file_to_send: str, new_filename: Optional[str] = None
) -> bool:
    try:
        await bot.send_document(
            chat_id=message.chat.id,
            document=InputFile(file_to_send, filename=new_filename),
        )
    except NetworkError:
        return False

    return True


async def send_documents(message: types.Message, pdf_path: str, docx_path: str) -> str:
    pdf_sent = await is_document_sent(message, pdf_path)
    docx_sent = await is_document_sent(message, docx_path)

    if pdf_sent and docx_sent:
        return "Conversion was successfully ended!"
    elif pdf_sent and not docx_sent:
        return "Conversion error: converted DOCX is to large (must be less than 50 MB)!"
    elif not pdf_sent and docx_sent:
        return "Conversion error: converted PDF is to large (must be less than 50 MB)!"
    return "Conversion failed because converted files are larger than 50MB!"
