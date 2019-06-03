# http://www.pythonchallenge.com/pc/return/evil.html

import os
import urllib.request


prompt = "http://www.pythonchallenge.com/pc/return/evil2.gfx"
prompt_top = "http://www.pythonchallenge.com/pc/return/"

username = "huge"
password = "file"

out_dir = "./_out/evil/"


def open_buffer():
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, prompt_top, username, password)
    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(handler)

    raw_data = opener.open(prompt).read()
    return raw_data


def main():
    buffer = open_buffer()

    # extracted from looking for headers in gfx's hex
    stacks = ["jpg", "png", "gif", "png", "jpg"]

    os.makedirs(out_dir)
    for i, ext in enumerate(stacks):
        file_path = os.path.join(out_dir, "{}.{}".format(i, ext))
        with open(file_path, 'wb') as out:
            out.write(buffer[i::5])

    return None


if __name__ == "__main__":
    print(main())


# http://www.pythonchallenge.com/pc/return/disproportional.html
