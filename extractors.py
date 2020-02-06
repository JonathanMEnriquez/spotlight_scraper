from lxml import html, etree
from constants import DETAIL_PAGE_XPATH, DETAIL_PAGE_IMG_XPATH, DETAIL_PAGE_CAPTION_XPATH, ID_PATH

# returns a list of all of the a tags
def extract_detail_page_href(html_content):
    href_list = []
    parts_path = DETAIL_PAGE_XPATH.split('SPLIT_HERE')
    for i in range(1,6):
        link_element = html_content.xpath(parts_path[0] + str(i) + parts_path[1])
        if link_element:
            href_list.append(link_element[0].attrib['href'])
    return href_list

def extract_image_src_from_detail_page(html_content):
    img = html_content.xpath(DETAIL_PAGE_IMG_XPATH)
    if img:
        return img[0].attrib['data-src']
    else:
        return None

def extract_location_from_detail_page(html_content):
    caption = html_content.xpath(DETAIL_PAGE_CAPTION_XPATH)
    if caption:
        return caption[0].text
    else:
        return None

def extract_id_from_url(_url):
    detail_id = _url.split('images/')
    if detail_id and len(detail_id) > 1:
        return detail_id[1]
    else:
        return None