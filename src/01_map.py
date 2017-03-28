# http://www.pythonchallenge.com/pc/def/map.html


prompt = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = "map"


def main():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    other = "cdefghijklmnopqrstuvwxyzab"

    translation_table = str.maketrans(alpha, other)
    print(prompt.translate(translation_table))

    return url.translate(translation_table)


if __name__ == "__main__":
    print(main())

# http://www.pythonchallenge.com/pc/def/ocr.html
