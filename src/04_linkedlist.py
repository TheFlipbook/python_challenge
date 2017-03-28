# http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib.request


url_root = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
prompt = "12345"

capture = ".html"


def main():
    next = prompt
    for x in range(400):
        data = str(urllib.request.urlopen(url_root + next).read(), "utf-8")

        next = data.split()[-1]  # Take last token
        print(next)

        if capture in data:
            return data

    return None


if __name__ == "__main__":
    print(main())

# http://www.pythonchallenge.com/pc/def/peak.html