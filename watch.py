import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r'src="https?://youtube.com/embed/([a-zA-Z0-9]+)"', s)
    if matches:
        result = matches.group(1)
        url = f"https://youtu.be/{result}"
        return url


if __name__ == "__main__":
    main()
