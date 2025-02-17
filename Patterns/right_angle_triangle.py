# *
# **
# ***
# ****
# *****

def triangle1(n):
    for i in range(n):
        for j in range(0,i+1):
            print("*", end="")
        print()

#triangle2
# 1
# 12
# 123
# 1234
# 12345

def triangle2(n):
    for i in range(1,n):
        for j in range(1,i): #Inner loop prints numbers from 1 to i
            print(j, end="")
        print()



#triangle3
# 1
# 22
# 333
# 4444
# 55555

def triangle3(n):
    for i in range(1,n):
        for j in range(0,i): #Inner loop prints 
            print(i, end="")
        print()

#reverse_triangle
# *****
# ****
# ***
# **
# *

def reverse_triangle(n):
    for i in range(n,0,-1):
        for j in range(i): #Inner loop prints 
            print('*', end="")
        print()

def main():
    n=int(input("Enter the number of lines :"))
    triangle1(n)
    triangle2(n)
    triangle3(n)
    reverse_triangle(n)

main()

