# http://www.pythonchallenge.com/pc/return/5808.html

from PIL import Image

import io
import urllib.request


prompt = "http://www.pythonchallenge.com/pc/return/cave.jpg"
prompt_top = "http://www.pythonchallenge.com/pc/return/"

username = "huge"
password = "file"


def open_image():
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, prompt_top, username, password)
    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(handler)

    raw_data = opener.open(prompt).read()

    buffer = io.BytesIO(raw_data)
    image = Image.open(buffer)

    return image


def main():
    image = open_image()
    width = image.width
    pixel_data = list(image.getdata())

    result = Image.new("RGB", (image.width // 2, image.height // 2))

    for row in range(image.height):
        offset = row % 2
        row_start = row * width
        row_end = (row+1) * width

        row_data = pixel_data[row_start:row_end]

        result_row = row // 2
        for x in range(width // 2):
            pixel = row_data[(x*2) + offset]
            result.putpixel((x, result_row), pixel)

    result.show()
    return result


if __name__ == "__main__":
    print(main())


# http://www.pythonchallenge.com/pc/return/evil.html
