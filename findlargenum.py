#Get inpurt from user
num1 = int(input("enter the number 1 to 100 : ---- "))
num2 = int(input("enter the number 1 to 100 : ---- "))
num3 = int(input("enter the number 1 to 100 : ---- "))

#define function to find largest number
def find_largestnumber(num,num2,num3):
 #usinng if else 
    if num1 > 95:
        print(":above 95:")
        largest = num1
    elif num2 < 90:
        print(":below 90:")
        largest = num2
    else:
        print("between 90 to 95")
        largest = num3
        #display the largest number
print("largest num is ",find_largestnumber(num1,num2,num3))
find_largestnumber( num1,num2,num3)