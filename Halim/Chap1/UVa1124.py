import sys

for line in sys.stdin:
    # I need to use end="", because the sys.stlin already reads the \n, and the
    # print() uses \n by default so we use two \n if we do nothing with the end=
    print(line, end="")