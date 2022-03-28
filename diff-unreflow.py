#!/usr/bin/env python3

import difflib
import sys

def words_with_map(lines):
    words = []
    word_line_numbers = {}
    for line_number, line in enumerate(lines):
        pos = len(words)
        words.extend([word.rstrip('\n') for word in line.split(' ')])
        for i in range(pos, len(words)):
            word_line_numbers[i] = line_number
    return (words, word_line_numbers)

with open(sys.argv[1]) as f_orig:
    l_orig = f_orig.readlines()

with open(sys.argv[2]) as f_patch:
    l_patch = f_patch.readlines()

w_orig, n_orig = words_with_map(l_orig)
w_patch, n_patch = words_with_map(l_patch)

line_number = 0
line_number_patch = 0
spaces = 0
s = difflib.SequenceMatcher(None, w_orig, w_patch)
for tag, i1, i2, j1, j2 in s.get_opcodes():
    #print('{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(
    #    tag, i1, i2, j1, j2, w_orig[i1:i2], w_patch[j1:j2]))
    if tag == 'equal':
        for index in range(i1, i2):
            word = w_orig[index]
            for _ in range(n_orig[index] - line_number):
                print()
                spaces = 0
            for _ in range(spaces):
                print(' ', end='')
            print(word, end='')
            spaces = 1
            line_number = n_orig[index]
        line_number_patch = n_patch[j2 - 1]

    if tag == 'insert' or tag == 'replace':
        for index_patch in range(j1, j2):
            word = w_patch[index_patch]
            if n_patch[index_patch] != line_number_patch:
                print()
                spaces = 0
            if word == '':
                spaces = spaces + 1
            else:
                for _ in range(spaces):
                    print(' ', end='')
                print(word, end='')
                spaces = 1
            line_number_patch = n_patch[index_patch]
        line_number = n_orig[i2 - 1]

    if tag == 'delete':
        line_number = n_orig[i2 - 1]

print()
