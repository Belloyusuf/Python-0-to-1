#! usr/bin/python3

# Python Assignment Operators

"""
Assume variable a holds 10 and variable b holds 20, then-

1. =                        Assigns values from right side operands to left side operand
2. += Add AND               It adds right operand to the left operand and assign the result to left operand
3. -= Subtract AND          It subtracts right operand from the left operand and assign the result to left operand        
4. *= Multiply AND          It multiplies right operand with the left operand and assign the result to left operand
5. /= Divide AND            It divides left operand with the right operand and assign the result to left operand
6. %= Modulus AND           It takes modulus using two operands and assign the result to left operand
7. **= Exponent AND         Performs exponential (power) calculation on operators and assign value to the left operand
8. //= Floor Division       It performs floor division on operators and assign value to the left operand

"""
a = 21
b = 10
c = 0

c = a + b
print ("Line 1 - Value of c is ", c)

c += a
print ("Line 2 - Value of c is ", c )

c *= a
print ("Line 3 - Value of c is ", c )

c /= a
print ("Line 4 - Value of c is ", c )

c = 2
c %= a

print ("Line 5 - Value of c is ", c)
c **= a
print ("Line 6 - Value of c is ", c)
c //= a
print ("Line 7 - Value of c is ", c)