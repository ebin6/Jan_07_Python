numbers=[23,12,9,13,7,10]
for num in numbers:
    if num <= 1:
        pass
    else:
        for i in range(2, num):
            if num % i == 0:
                break
        else: 
            print(num,end=" ")
