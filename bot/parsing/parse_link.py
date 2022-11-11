from youtubesearchpython import VideosSearch


def parse_link(i, serch_term):
    videos_search = VideosSearch(f'{serch_term}', limit=i)
    return str(videos_search.result())


def links_split(serch_term):
    list_of_links = []
    for i in range(1, 6):
        result_str = parse_link(i, serch_term)
        result_str = result_str.split("'link': ")[-1]
        result_str = result_str.split(",")[0]
        result_str = result_str.strip("'")
        i += 1
        list_of_links.append(result_str)

    return list_of_links
