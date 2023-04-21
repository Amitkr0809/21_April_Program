# Conditional statements

# 1) if statement

i= 5
if i in range(1,10):
    print(i)

# 2) if_else Statement

n = int(input ("enter number : "))
if n / 2 == '0':
    print("number is even")
else:
    print("Number id odd")

# 3)  if_elif_else statement

num = int(input ("enter number : "))
if num < 0:
    print("Number is negative")
elif num > 0:
    print ("Number is Positive")
else:
    print("number is Zero")


# 4) Nested if

num = int(input ("enter number : "))
if num < 0:
    print("Number is negative")
if num > 0:
    print ("Number is Positive")
else:
    print("number is Zero")