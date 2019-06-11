# http://www.pythonchallenge.com/pc/bin/hex.html


import bz2
import io
import urllib.request
import urllib.error
import zipfile
import zlib


out_dir = "_out/idiot"

prompt = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
prompt_top = "http://www.pythonchallenge.com/pc/hex/"
prompt_range = 1152983631
prompt_pass = b"redavni"

username = "butter"
password = "fly"


def open_section(start=None):
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, prompt_top, username, password)
    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(handler)

    headers = {}
    if start:
        headers["Range"] = "bytes={}-".format(start)

    request = urllib.request.Request(prompt, headers=headers)
    response = opener.open(request)

    return response.read()


def main():
    data = open_section(start=prompt_range)

    stream = io.BytesIO(data)
    archive = zipfile.ZipFile(stream)

    # Get Prompt
    with archive.open("readme.txt", pwd=prompt_pass) as readme:
        text = (b"".join(readme.readlines())).decode("ascii")
        print(text)

    # Inspect data
    with archive.open("package.pack", pwd=prompt_pass) as package:
        generation = package.read()

        # Data ping-pongs between compression methods
        zlib_header = b"x"
        bz2_header = b"BZh"

        # Reversing twice means we couldn't find a header
        just_reversed = False
        for x in range(2000):

            if generation.startswith(zlib_header):
                print("_", end=" ")
                just_reversed = False
                generation = zlib.decompress(generation)

            elif generation.startswith(bz2_header):
                print("B", end=" ")
                just_reversed = False
                generation = bz2.decompress(generation)

            elif just_reversed:
                break

            else:
                print("f")
                just_reversed = True
                generation = generation[::-1]

        print(generation)

    return archive


if __name__ == "__main__":
    print(main())


# http://www.pythonchallenge.com/pc/hex/copper.html
