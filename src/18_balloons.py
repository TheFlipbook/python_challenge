# http://www.pythonchallenge.com/pc/return/balloons.html
# http://www.pythonchallenge.com/pc/return/brightness.html


import difflib
import gzip
import os
import urllib.request
import urllib.parse

prompt = "http://www.pythonchallenge.com/pc/return/deltas.gz"
prompt_top = "http://www.pythonchallenge.com/pc/return/"

username = "huge"
password = "file"
out_dir = "_out/balloons"


def open_buffer():
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, prompt_top, username, password)
    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(handler)

    raw_data = opener.open(prompt).read()

    return raw_data


def main():
    result = open_buffer()
    data = gzip.decompress(result)

    left = []
    right = []

    lines = data.decode("utf-8").split("\n")

    for line in lines:
        half = len(line) // 2

        left_line = line[:half].strip()
        right_line = line[half:].strip()

        left.append(left_line)
        right.append(right_line)

    diff = difflib.Differ().compare(left, right)

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    with open(os.path.join(out_dir, "left.png"), "wb") as left_file:
        with open(os.path.join(out_dir, "right.png"), "wb") as right_file:
            with open(os.path.join(out_dir, "both.png"), "wb") as both_file:
                for line in diff:
                    clean = line.strip("-+ ")
                    data = bytes.fromhex(clean.replace(" ", ""))

                    if line.startswith("-"):
                        left_file.write(data)
                    elif line.startswith("+"):
                        right_file.write(data)
                    else:
                        both_file.write(data)

    return diff


if __name__ == "__main__":
    print(main())


# http://www.pythonchallenge.com/pc/hex/bin.html
# butter, fly
