#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "KashFar with Piero's assistance"


"""Properly Nested Brackets:

In this problem we consider expressions containing brackets that are
    properly nested. These expressions are obtained by juxtaposition of
    properly nested expressions in a pair of matching brackets,
    the left one an opening and the right one a closing bracket.

    ( a + $ ( b = ) ( a ) )    # this is properly nested

    ( a + $ ) b = ) ( a ( )    # this is not

    The pairs of brackets are:
    (  )
    [  ]
    {  }
    <  >
    (*  *)

    The output is a textfile named output.txt. Each line contains the
    result of the check of the corresponding inputline, that is ‘YES’
    (in upper case), if the expression is OK, and (if it is not OK)
    ‘NO’ followed by a space and the position of the error.
"""

import sys


def valid_parentheses(string):
    "Checks for properly nested brackets. Then returns index if unbalanced."
    opener_list = ['(', '[', '{', '<', '(*']
    closer_list = [')', ']', '}', '>', '*)']

    index = 0
    stack = []

    while string:
        token = string[0]
        if string[:2] == '(*' or string[:2] == '*)':
            token = string[:2]
        index += 1
        string = string[len(token):]
        if token in opener_list:
            stack.append(token)
        elif token in closer_list:
            matching_opener = opener_list[closer_list.index(token)]
            if stack.pop() != matching_opener:
                return ("NO", index)
    if not stack:
        return "YES"
    else:
        return ("NO", index)


def main(args):
    """Opens the file and feeds it into our checker. Creates an output.txt
    file writes ok or no inside of it."""
    with open("input.txt", "r") as opened_file:  # this is an iterable
        with open("output", "w") as output:
            for line in opened_file:
                result = valid_parentheses(line)
                output.write(str(result) + "\n")


if __name__ == '__main__':
    main(sys.argv)
