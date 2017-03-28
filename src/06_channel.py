# http://www.pythonchallenge.com/pc/def/channel.html

import io
import urllib.request
import zipfile


prompt = "http://www.pythonchallenge.com/pc/def/channel.zip"
first = "90052"
file_format = "{}.txt"


def main():
    raw_data = urllib.request.urlopen(prompt).read()
    buffer = io.BytesIO(raw_data)
    archive = zipfile.ZipFile(buffer)
    archive_files = [info.filename for info in archive.filelist]

    next = first

    output = []
    for x in range(8000):
        file_path = file_format.format(next)

        if file_path in archive_files:
            file_data = str(archive.open(file_path).read(), "utf-8")

            next = file_data.split()[-1]  # Take last token

            result = str(archive.getinfo(file_path).comment, "utf-8")
            output.append(result)

        else:
            break

    return "".join(output)


if __name__ == "__main__":
    print(main())

# http://www.pythonchallenge.com/pc/def/hockey.html
# http://www.pythonchallenge.com/pc/def/oxygen.html