def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

for i in range(5):
    print("Whatever statements are not in a control block will run regardless.")


if __name__ == "__main__":
    # Code inside this block will only run when wc.py is executed as the main program,
    # not when it is imported as a module.
    print(linecount('wc.py'))
else:
    print("We usually avoid an else conditional --> AnYWaY: explicitly call it")