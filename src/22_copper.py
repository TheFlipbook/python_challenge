# http://www.pythonchallenge.com/pc/bin/hex.html


from PIL import Image, ImageDraw, ImageSequence
import io
import urllib.request
import urllib.error


prompt = "http://www.pythonchallenge.com/pc/hex/white.gif"
prompt_top = "http://www.pythonchallenge.com/pc/hex/"

username = "butter"
password = "fly"


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

    result = Image.new("RGB", (1000, 1000))
    draw = ImageDraw.Draw(result)

    center = ((image.width // 2), (image.height // 2))
    cursor = [500, 500]

    # Animated Gif
    trace = []
    spacing = 25
    far_right = cursor[0]

    for frame in ImageSequence.Iterator(image):
        min_x, min_y, max_x, max_y = frame.getbbox()

        centroid_x = (max_x + min_x) // 2
        centroid_y = (max_y + min_y) // 2

        move_x = (centroid_x - center[0])
        move_y = (centroid_y - center[1])

        if not (move_x or move_y):
            draw.line(trace)
            trace = []
            cursor[0] = far_right + spacing

        cursor[0] += move_x
        cursor[1] += move_y

        if cursor[0] > far_right:
            far_right = cursor[0]

        trace.append(tuple(cursor))

    draw.line(trace)

    result.show()
    return result


if __name__ == "__main__":
    print(main())


# http://www.pythonchallenge.com/pc/hex/bonus.html
