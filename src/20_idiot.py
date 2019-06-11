# http://www.pythonchallenge.com/pc/bin/hex.html


import os
import urllib.request
import urllib.error


out_dir = "_out/idiot"

prompt = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
prompt_top = "http://www.pythonchallenge.com/pc/hex/"

username = "butter"
password = "fly"


def split_range_data(response_string):
    prefix, sep, numbers = response_string.partition(" ")
    range_numbers, sep, total = numbers.partition("/")
    low, sep, high = range_numbers.partition("-")
    return int(low), int(high), int(total)


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

    low, high, total = split_range_data(response.headers["Content-Range"])
    raw_data = response.read()

    return low, high, total, raw_data


def main():
    start = None
    end = None

    results = []

    # The server only served back part of the content
    # So, iterate through chunks "beyond" the image
    for i in range(20):
        try:
            low, high, total, data = open_section(start=start)
            results.append(str(data))

            start = high + 1
            end = total

        except urllib.error.HTTPError:
            # Couldn't get data for range, done with this search
            break

    # Now check passed the end of the whole range
    low, high, total, data = open_section(start=(end+1))
    results.append(str(data[::-1]))

    # We got back a different start than we asked for
    #  We asked at the end, so search "in"
    low, high, total, data = open_section(start=(low-1))
    results.append(data.decode("ascii"))

    for result in results:
        print(result)

    # Rip the target range out of the custom string
    junk, sep, location = results[-1].strip("\n.").rpartition(" ")
    low, high, total, data = open_section(start=location)

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # Write out the discovered file
    #  Bytes start with "PK" so we know it's a zip.
    with open(os.path.join(out_dir, "solution.zip"), "wb") as writer:
        writer.write(data)

    return data


if __name__ == "__main__":
    print(main())


# http://www.pythonchallenge.com/pc/hex/unreal.jpg
# Content-Range: 1152983631
