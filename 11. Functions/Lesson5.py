def addNumber(num, *args, **kwargs):
    result = num  # Start with the initial value of num
    
    for number in args:
        result += number  # Add each additional number in args to result
    
    print(result, **kwargs)  # Print the final result using kwargs

# Test the function with the given numbers
addNumber(2, 3, 4, 5)  # Expect 14
