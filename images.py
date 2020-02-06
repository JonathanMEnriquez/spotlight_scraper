import requests
import os.path
from PIL import Image
from lxml import html
from constants import ABS_PATH

def download_image(src):
    downloaded = requests.get(src)
    try:
        return downloaded.content
    except:
        return None

def save_image_to_file(src, caption):
    caption += '.jpg'
    filename = os.path.join(ABS_PATH, caption)
    img_content = download_image(src)
    if img_content and caption:
        try:
            with open(filename, 'wb') as img:
                img.write(img_content)
        except:
            raise FileNotFoundError('Could not open file ' + caption + '.jpg')