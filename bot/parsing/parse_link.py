from youtubesearchpython import VideosSearch


def parse_link(i: int, search_term: str) -> str:
    videos_search = VideosSearch(f"{search_term}", limit=i)
    return str(videos_search.result())


def links_split(search_term: str) -> list:
    list_of_links = []
    for i in range(1, 6):
        result_str = parse_link(i, search_term)
        result_str = result_str.split("'link': ")[-1]
        result_str = result_str.split(",")[0]
        result_str = result_str.strip("'")
        list_of_links.append(result_str)

    return list_of_links
