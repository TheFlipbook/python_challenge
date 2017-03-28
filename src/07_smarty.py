# http://www.pythonchallenge.com/pc/def/oxygen.html

from PIL import Image

import io
import urllib.request
import ast

prompt = "http://www.pythonchallenge.com/pc/def/oxygen.png"
target_row = 50
target_stride = 7

def main():
    raw_data = urllib.request.urlopen(prompt).read()
    buffer = io.BytesIO(raw_data)
    image = Image.open(buffer)

    steno_data = []
    for i in range(0, image.width, target_stride):
        pixel = image.getpixel((i, target_row))

        r, g, b, a = pixel
        if r == g and g == b:
            steno_data.append(chr(r))

    message = "".join(steno_data)

    comment, sep, chunk = message.partition("[")
    real_data = ast.literal_eval("[" + chunk)

    output = []
    for item in real_data:
        output.append(chr(item))

    return "".join(output)


if __name__ == "__main__":
    print(main())

# http://www.pythonchallenge.com/pc/def/integrity.html
