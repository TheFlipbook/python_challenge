# http://www.pythonchallenge.com/pc/return/romance.html


import urllib.request
import urllib.parse
import http.cookiejar
import bz2
import xmlrpc.client


def open_cookie(url):
    cookie_jar = http.cookiejar.CookieJar()
    cookie_handler = urllib.request.HTTPCookieProcessor(cookie_jar)
    opener = urllib.request.build_opener(cookie_handler)

    response = opener.open(url)

    data = str(response.read(), "utf-8")
    link = data.split()[-1]  # Take last token

    # If not an integer, stop iteration
    try:
        int(link)
    except ValueError:
        link = None

    cookie_values = []
    for cookie in cookie_jar:
        parsed = cookie.value.replace("+", " ")
        as_bytes = urllib.parse.unquote_to_bytes(parsed)
        cookie_values.append(as_bytes)

    return link, cookie_values


def phase_00():
    # image in bottom corner is for "linkedlist"
    #  Prompt from getting cookies from romance is "you should have followed busynothing"
    url_root = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
    prompt = "12345"

    message = []

    query = prompt
    for x in range(400):
        query, cookie = open_cookie(url_root + query)
        if cookie:
            message.extend(cookie)

        if not query:
            break

    # values started with "BZh" header for Bzip2
    byte_data = b"".join(message)
    result = bz2.decompress(byte_data)
    return result


def phase_01():
    url = "http://www.pythonchallenge.com/pc/phonebook.php"
    rpc = xmlrpc.client.ServerProxy(url)
    result = rpc.phone("Leopold")  # Mozart's father.
    return result


def phase_02():
    url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
    message = "the flowers are on their way"  # from phase_00
    cookie = "info=" + message
    headers = {"Cookie": cookie}
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    return response.read()


def main():
    print(phase_00())  # "Call his father"
    print(phase_01())  # "555-VIOLIN"
    print(phase_02())  # "don't you dare to forget the balloons"
    return


if __name__ == "__main__":
    print(main())


# b'is it the 26th already? call his father and inform him that "the flowers are on their way". he\'ll understand.'
# http://www.pythonchallenge.com/pc/stuff/violin.php
# http://www.pythonchallenge.com/pc/return/balloons.html
