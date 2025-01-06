# -*- coding: utf-8 -*-
"""replacingCharacterinString.ipynb


https://learn.codesignal.com/course/247/unit/1/practice/2
Given a string, you need to return a new string where every letter is shifted to its right by one place in alphabetical order. 
The last letters z and Z should be replaced with the first ones: a and A, respectively. If the character isn't a letter, 
it should stay the same.


For example, given the string "abc123XYz!", the function should return "bcd123YZa!".
"""

def solution(s):
    # TODO: Implement the solution here
    newstring = ''
    for i in s:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            if i == 'z':
                newstring += 'a'
            elif i == 'Z':
                newstring += 'A'
            else:
                new_letter = ord(i) + 1
                newstring += chr(new_letter)
        else:
            newstring += i
    return newstring

