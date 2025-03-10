# https://learn.codesignal.com/course/247/unit/1/practice/5
# You are given a string s. Your task is to write a function that returns a string in which every pair of adjacent characters in the original string is swapped. If the string has an odd length, leave the last character as it is.

# It is not allowed to use Python built-in functions like reverse() or join() in this task, you should implement the solution without using them.

# For example, if you are given the string "abcdef", your function should return "badcfe". If the string is "hello", your function should return "ehllo".

def solution(s):
    swapped_chr=""
    for i in range(0, len(s) - 1, 2):
        swapped_chr+=s[i+1]
        swapped_chr+=s[i]
        
    if len(s)%2 !=0:
        swapped_chr+=s[-1]
             
    return swapped_chr

print(solution("helloWorld"))