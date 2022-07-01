def add(num1, num2):
    return num1+num2


def multiply(num1, num2):
    return num1*num2


def subtract(num1, num2):
    return num1-num2


def lambda_handler(event, context):
    num1 = event['Number-1: ']
    num2 = event['Number-2: ']
    a = add(num1, num2)
    b = multiply(num1, num2)
    c = subtract(num1, num2)
    print(a)
    print(b)
    print(c)
