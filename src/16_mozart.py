# http://www.pythonchallenge.com/pc/return/mozart.html


from PIL import Image

import io
import urllib.request
import itertools

prompt = "http://www.pythonchallenge.com/pc/return/mozart.gif"
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
    rgb_image = image.convert("RGB")
    sentinel = (255, 0, 255)

    result = Image.new("RGB", image.size)
    for row in range(image.height):
        start = 0
        for x in range(image.width):
            pixel = rgb_image.getpixel((x, row))
            if pixel == sentinel:
                start = x
                break

        for x in range(image.width):
            offset = (x + start) % image.width
            result.putpixel((x, row), rgb_image.getpixel((offset, row)))

    result.show()
    return result


if __name__ == "__main__":
    print(main())


# http://www.pythonchallenge.com/pc/return/romance.html
