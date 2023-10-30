#!/usr/bin/python

def by_value(e):
    return e[1]

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    letter_count = {}
    for ch in file_contents.lower():
        if ch in letter_count:
            letter_count[ch] += 1
        elif ch.isalpha():
            letter_count[ch] = 1
    count = list(letter_count.items())
    count.sort(key=by_value, reverse=True)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document\n")
    for t in count:
        print(f"The '{t[0]}' character was found {t[1]} times")

    print("--- End report ---")
