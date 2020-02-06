import requests
from lxml import html, etree
from extractors import extract_detail_page_href, extract_image_src_from_detail_page, extract_location_from_detail_page, extract_id_from_url
from images import save_image_to_file
from constants import MAIN_URL
from write_to_file import write_to_json_file
from PIL import Image

COUNTER = 1
counter_is_valid = True
entries = []

while counter_is_valid:
    page = requests.get(MAIN_URL + str(COUNTER))

    if not page.status_code is 200:
        counter_is_valid = False
    else:
        try:
            tree = html.fromstring(page.content)
            detail_links = extract_detail_page_href(tree)
            data = dict()
        except:
            COUNTER += 1
            pass
        else:
            for link in detail_links:
                if link:
                    d_page = requests.get(link)
                    d_tree = html.fromstring(d_page.content)
                    caption = extract_location_from_detail_page(d_tree)
                    link_id = extract_id_from_url(link)
                    img_src = extract_image_src_from_detail_page(d_tree)

                    if caption and link_id and img_src:
                        data['caption'] = caption
                        data['id'] = link_id
                        data['img_src'] = img_src
                        print(data)
                        entries.append(data)
                        write_to_json_file('contents.json', entries)

                    # If you want to save the images as well uncomment below

                    # if caption and img_src:
                    #     caption = caption.replace(' ', '_')
                    #     try:
                    #         save_image_to_file(img_src, caption)
                    #     except FileNotFoundError as e:
                    #         print(e)
                    #         print('Failed at page: ' + str(COUNTER))
                    #     except Exception:
                    #         pass
            COUNTER += 1

print('SCRAPING COMPLETE!!')