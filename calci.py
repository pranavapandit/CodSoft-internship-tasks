print("select the arithmetic operation")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")

while True:
    operation = int(input("enter the choice(1/2/3/4)>>"))
    num1 = float(input("Enter num1>>  "))
    num2 = float(input("Enter num2>>  "))
    
    if operation==1:
        print(num1+num2)
    elif operation==2:
        print(num1-num2)
    elif operation==3:
        print(num1*num2)
    elif operation==4:
        print(num1/num2)
    elif operation==0:
        break
    else:
        print("invalid")