# print prime number using range from(1,100)


for i in range (1,100):
    for j in range(1,100):
        if i == j:
            if i % j == 0 :
                print(i)