# ****
# ****
# ****
# ****

def square(n):
    for i in range(0,n,1):
        for j in range(0,n,1):
            print("*", end="")
        print()

def main():
    n=int(input("Enter the number of lines :"))
    square(n)
main()

#in Javascript
# for (let i =0;i<4;i++){
#     for (let j=0;j<4;j++){
#         process.stdout.write("*"); 
#     }
#     console.log()

# }