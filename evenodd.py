#check even or odd number

num = int(input("enter a number: "))
if num % 2 ==0:
    print(f"{num} even number")
elif num % 2 != 0:
    print(f"{num} odd number")



#factorial

X = int(input("Enter first factorial number: "))

for i in range(1,X):

    X = X * i

print(X)