# http://www.pythonchallenge.com/pc/def/peak.html

import pickle
import urllib.request


prompt = "http://www.pythonchallenge.com/pc/def/banner.p"


def main():
    raw_data = urllib.request.urlopen(prompt).read()
    data = pickle.loads(raw_data)

    output = []
    for row in data:
        line = []
        for letter, count in row:
            line.append(letter*count)
        output.append("".join(line))


    return "\n".join(output)


if __name__ == "__main__":
    print(main())

# http://www.pythonchallenge.com/pc/def/channel.html
