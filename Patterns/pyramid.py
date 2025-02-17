
#     *         4 - 1- 4   
#    ***        3 - 3- 4
#   *****       2 - 5- 2
#  *******      1 - 7- 1
# *********     0 - 9- 0


#space     print       space   n=5
# n-i-1    2*i-1       n-i-1
def pyramid(n):
    for i in range(n):
        print(" ", end="")
        for j in range(n-i-1):
            print(" ", end="")
        for k in range(2*i+1):
            print("*", end="")

        print()

def main():
    n=int(input("Enter the number of lines :"))
    pyramid(n)

main()