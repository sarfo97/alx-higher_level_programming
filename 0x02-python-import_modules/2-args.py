#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Get all arguments except the script name
    argc = len(argv)  # Number of arguments

    if argc == 0:
        print(f"{argc} arguments.")
    elif argc == 1:
        print(f"{argc} argument:")
    else:
        print(f"{argc} arguments:")

    for i, arg in enumerate(argv, 1):
        print(f"{i}: {arg}")

