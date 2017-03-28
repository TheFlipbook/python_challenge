# http://www.pythonchallenge.com/pc/def/integrity.html

import bz2


prompt = "http://www.pythonchallenge.com/pc/return/good.html"
top_level_url = "http://www.pythonchallenge.com/pc/return/"

prompt_un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
prompt_pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'


def main():

    parse_un = bz2.decompress(prompt_un)
    parse_pw = bz2.decompress(prompt_pw)

    return parse_un, parse_pw


if __name__ == "__main__":
    print(main())


# http://www.pythonchallenge.com/pc/return/good.html
