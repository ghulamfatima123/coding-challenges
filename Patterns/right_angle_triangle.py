# *
# **
# ***
# ****
# *****

def triangle(n):
    for i in range(n):
        for j in range(0,i+1):
            print("*", end="")
        print()

def main():
    n=int(input("Enter the number of lines :"))
    triangle(n)
main()
