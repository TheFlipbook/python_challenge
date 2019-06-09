# http://www.pythonchallenge.com/pc/return/cat.html
# http://www.pythonchallenge.com/pc/return/uzi.html


import calendar
import datetime


def main():
    valid = []

    # Iterate "1__6" years to match Calendar image
    for year in range(1006, 2000, 10):
        # Calendar shows Feb 29, must be a leap year
        if calendar.isleap(year):

            # Day after marked day is Tuesday, January 27th
            target = datetime.date(year, 1, 27)
            if target.weekday() == calendar.TUESDAY:
                valid.append(target)

    # "he ain't the youngest, he is the second"
    final = valid[-2]
    return final


if __name__ == "__main__":
    print(main())


# Wolfgang Amadeus Mozart, born on January 27, 1756
# http://www.pythonchallenge.com/pc/return/mozart.html
