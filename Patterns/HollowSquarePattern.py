# *****
# *   *
# *   *
# *   *
# *****

def H_square(n):
    for i in range(0,n):
        if i==0 or i==n-1:
            print('*'*n)
        else:
            print("*"+ " "*(n-2)+ "*" )
        

def main():
    n=int(input("Enter the number of lines :"))
    H_square(n)
main()

# mid-? (1 ≤ i ≤ n-2) → Print *, then spaces, then *.