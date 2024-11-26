print("Welcome to Saddam Calculator")

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

while True:
    operation = input("Enter operation to work(+,-,* or /) : ")

    if operation in ["+","-","*","/"]:
        firstNum = int(input("Enter first Number : "))
        secondNum = int(input("Enter Second Number : "))


        if operation == "+":
            result = add(firstNum,secondNum)
        elif operation == "-":
            result = subtract(firstNum,secondNum)
        elif operation == "*":
            result = multiply(firstNum,secondNum)
        elif operation == "/":
            if secondNum == 0:
                print("Can't divide number by zero")
                continue
            result = divide(firstNum,secondNum)
        
        print(result)
        next_operation = input("Do you want to perform another operation? y / n : ")
        if next_operation == 'y':
            continue
        else:
            break
    else:
        print("Invalid Input!Enter either (+ , - , * or / )")
        continue




