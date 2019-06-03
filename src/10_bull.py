# http://www.pythonchallenge.com/pc/return/bull.html

# Question: len(a[30]) = ?
# Prompt: a = [1, 11, 21, 1211, 111221,
# 1
# 1 1
# 2 1
# 1 2 1 1
# 1 1 1 2 2 1
# 3 1 2 2 1 1
# 1 3 1 1 2 2 2 1


def generate(prompt):
    seq = []

    tally = 1
    target = prompt[0]

    for item in prompt[1:]:
        if item == target:
            tally += 1

        else:
            seq.extend((tally, target))

            tally = 1
            target = item

    if target is not None:
        seq.extend((tally, target))

    return seq


def main():
    prompt = [1]
    for x in range(30):
        prompt = generate(prompt)

    return len(prompt)


if __name__ == "__main__":
    print(main())


# http://www.pythonchallenge.com/pc/return/5808.html
