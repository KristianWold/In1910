#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def count_chars(string):
    chars = {}
    string = string.lower()
    for i in range(len(string)):
        if string[i] in chars:
            chars[string[i]] += 1
        else:
            chars[string[i]] = 1
    return chars

example = "Hello, world!"
for char, count in count_chars(example).items():
    print('{:3}{:10}'.format(char, count))

print("In alphabetical order")

for char, count in sorted(count_chars(example).items()):
    print('{:3}{:10}'.format(char, count))
