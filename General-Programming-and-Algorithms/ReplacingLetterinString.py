# -*- coding: utf-8 -*-
"""ReplacingLetterinString.ipynb


https://learn.codesignal.com/course/247/unit/1/practice/4
Given a string input_string, return a new string in which all occurrences of character c1 
in the original string replaced by c2. You cannot use any built-in string methods or functions in Python, 
such as replace().

Here's an example:

print(replace_character("hello, world", "o", "a"))  
# Output: "hella, warld"
In this example, all occurrences of o have been replaced by a.
"""

def replace_character(input_string, c1, c2):

    result = ""

    for char in input_string:
        if char == c1:  # If character matches c1, replace it with c2
            result += c2
        else:  # Otherwise, keep the original character
            result += char

    return result

print(replace_character("hello, world", "o", "a"))


