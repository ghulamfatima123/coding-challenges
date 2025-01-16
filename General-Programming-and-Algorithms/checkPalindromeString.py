#https://learn.codesignal.com/course/247/unit/1/practice/6

# You are given a string, and your task is to check whether the provided string is a palindrome, without using any built-in string methods. A string is a palindrome if it reads the same forward and backward, ignoring the casing of letters ('A' and 'a' are considered the same) and ignoring non-letter characters.

# Return a boolean value: True if the string is a palindrome and False if it is not.

# It is not allowed to use Python built-in functions like reverse(), reversed(), or similar in this task.

def solution(input_string):
    filtered_result=''
    rev_str=''
    for i in input_string:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            if 'a' <= i <= 'z':
                filtered_result+= chr(ord(i)-32)
            else:
                filtered_result+=i
    for i in range(len(filtered_result)-1,-1,-1):
        rev_str+=filtered_result[i]
                      
    if filtered_result==rev_str:
        return True
    
    return False
        

    
        
        
print(solution("!@#$%^&*()"))

