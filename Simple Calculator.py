operator = input("Enter an operation + - * / or **.5: ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+" :
    result = num1+num2
    print(round(result , 5))
elif operator == "-" :
    result = num1-num2
    print(round(result , 5))
elif operator == "*" :
    result = num1*num2
    print(round(result , 5))
elif operator == "/" :
    result = num1/num2
    print(round(result , 10))
elif operator == "**.5" :
    result = num1**0.5
    print(round(result , 20))
else : 
    print(f"{operator} isn't a valid operation")