# Print different patterns

for i in range (5,0,-1):
    print(i * "* ")


for i in range (1,6):
    print(i * "* ")


for i in range (1,6):
    print(i,i+5)


for i in range (1,4):
    if i == 1:
        print(i)
    elif i == 2:
        print(i * "2")
    else:
        print(i * "3")


for i in range (1,6):
    for j in range (0,i):
        print(i,end=" ")
    print()


for i in range (1,11):
    if i == 1:
        print(i)
    elif i == 2:
        print(i,i+1)
    elif i == 4:
        print(i,i+1,i+2)
    elif i == 7:
        print(i,i+1,i+2,i+3)
