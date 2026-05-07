'''word=input("Enter the string : ")

count=dict()
for k in word:
   if k in count:
        count[k]=count[k]+1    
   else:
        count[k]=1
   print(count)
print(count)
'''
for num in range(3,8):
     fact=1
     for k in range(1,num+1):
          fact*=k
     print(f"Factorial of {num} is {fact}")


print("Using while loop")
num=3
while num<=7:
     count=fact=1
     while count<=num:
          fact*=count
          count+=1
     print(f"Factorial of {num} is {fact}")
     num+=1 