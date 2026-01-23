'''name="Ebin"
for s in name:    
    print(s)


for num in range(1,11):
    print(num)'''

'''number=5
for n in range(1,11):
    print(f"{n} * {number} = {number*n}"

    # print(n,"*",number,"=", number*n)'''

'''numbers=[12,4,3,2]
sum=0
for k in numbers:
    sum=sum+k  # sum+=k

print(sum)'''

'''
while condition:
    statements 
    
'''
'''num=int(input("Enter the number : "))
c=1
fact=1
while c<=num:
    fact=fact*c
    c+=1
print(fact) '''

'''numbers=[]
size=int(input("Enter the list size : "))
for n in range(size):
    num=int(input("Enter the number : "))
    numbers=numbers+[num]
sum=0
for k in numbers:
    sum=sum+k  # sum+=k

print(sum)'''

'''numbers=[5,2,4]
for n in numbers:
    fact=1
    for k in range(1,n+1):
        fact=fact*k
    print(f"Factorial of {n} = {fact}")'''

first,second=0,1
print(first,second,end= " ")
for num in range(8):
    third=first+second
    print(third,end=" ")
    first,second=second,third
