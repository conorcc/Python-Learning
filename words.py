# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.

# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import urllib


def fetch_words(url):
    story = urllib.urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(story_words):
    for word in story_words:
        print(word)


def main():
    url = sys.argv[1]
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main()
