from bs4 import BeautifulSoup

def get_items_where_href_contains_markers(page_content, *markers):
    result = []
    all_a_elements = page_content.findAll('a')
    for a_element in all_a_elements:
        try:
            if any(x in a_element.attrs['href'] for x in markers):
                result.append(a_element)
        except KeyError:
            pass
    return result


def get_items_where_src_contains_markers(page_content, *markers):
    result = []
    all_video_elements = page_content.findAll('source')
    for video_element in all_video_elements:
        try:
            if any(x in video_element.attrs['src'] for x in markers):
                result.append(video_element)
        except KeyError:
            pass
    return result


def remove_duplicates_and_clear(raw_list):
    # entfernt Duplicate und Elemente ohne Text
    result = {}
    for element in raw_list:
        try:
            if element.attrs['href'] not in result:
                if str(element.text) is not None:
                    if str(element.text).strip():
                        result[element.attrs['href']] = element
        except KeyError:
            if element.attrs['src'] not in result:
                result[element.attrs['src']] = element
    return list(result.values())
