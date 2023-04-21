# Explain about Operators in python with 2 examples by writing code .
'''
1) - Arithmatic Operators-- Addition(+), Subtraction(-), Multiplication(*), Division(/), Floor division(//), modulos(%),
Power(**)'''

a = 10
b = 2
print("a+b = ",a+b)
print("a-b = ", a-b)

'''
2) Assignment Operators -- Assignment(=),Addition Assignment(+=),Subtraction Assignment(-=), Multiplication Assignment(*=),
Division Assignment(/=), Remainder Assignment(%=), Exponent Assignment(**=) '''

a = 10
print(a)
a += 1
print(a)

"""
3) Comparison or relational Operators -- Equal to(==),Not equal to(!=), Less than(<), Grater than(>),
Less than equal to(<=), Grater than equal to(>=), 
 """
print(1 == 1)
print( 2!= 1)

"""
4) Logical Operators -- and , or, Not """

a=1
b=2
print(a and b)
print(a or b)
print(not b)

"""
5) Membership Operators -- in , not in """

l= [1,2,3,4,5]
for i in l:
    print(i)

print(2 not in l)

"""
6) Bitwise Operators -- Bitwise And(&), Bitwise or(|), Bitwise xor (^), Bitwise not(~), left shift(<<),
Right shift(>>) """

a = 2
b = 3
print(a&b)
print(a|b)