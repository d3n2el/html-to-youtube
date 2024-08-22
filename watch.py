import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r"(?<=https://www.youtube.com/embed/).*", s)
    print(matches)
    if matches:
        result= matches.group
        url= f"https://youtu.be/{result}"
        return url


...


if __name__ == "__main__":
    main()
