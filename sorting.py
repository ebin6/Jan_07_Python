'''l=[8,4,2,1,7]
length=len(l)
for i in range(length):
    for j in range(length-i-1):
        print('j = ',j)
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
        print(l)
print(l)'''