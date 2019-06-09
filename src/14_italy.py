# http://www.pythonchallenge.com/pc/return/italy.html

from PIL import Image

import io
import urllib.request
import itertools

prompt = "http://www.pythonchallenge.com/pc/return/wire.png"
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


def iter_spiral(width, height):
    dirs = itertools.cycle([(1, 0), (0, 1), (-1, 0), (0, -1)])
    x = 0
    y = 0
    direction = next(dirs)

    bounds_low_x = 0
    bounds_low_y = 1  # pre-pump because it's as if we turned the first corner
    bounds_high_x = width-1
    bounds_high_y = height-1

    for i in range(width * height):
        yield (x, y)

        corner = False

        if (direction[0] < 0) and (x <= bounds_low_x):
            bounds_low_x += 1
            corner = True
        elif (direction[1] < 0) and (y <= bounds_low_y):
            bounds_low_y += 1
            corner = True
        elif (direction[0] > 0) and (x >= bounds_high_x):
            bounds_high_x -= 1
            corner = True
        elif (direction[1] > 0) and (y >= bounds_high_y):
            bounds_high_y -= 1
            corner = True

        if corner:
            direction = next(dirs)

        x += direction[0]
        y += direction[1]

    return


def main():
    image = open_image()
    dimensions = (100, 100)
    pixels = image.getdata()

    result = Image.new("RGB", dimensions)
    for i, coord in enumerate(iter_spiral(*dimensions)):
        result.putpixel(coord, pixels[i])

    result.show()
    return image


if __name__ == "__main__":
    print(main())


# http://www.pythonchallenge.com/pc/return/cat.html
