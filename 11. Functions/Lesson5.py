# lesson 5 on function

def addNumber(num, *args, **kwargs):
    result =  num 
    for number in args:
        result += number
    print(result, **kwargs)

addNumber(2, 3, 4, 5)