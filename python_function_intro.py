'''
def greeting(name,age,place="Kochi"):  # Function defination
    print(f"Hello {name} , you are {age} years old and you from {place}")

greeting("Ebin",27)

greeting("Joyal",21,"Vaikom")'''

"""
def evenOdd(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")

evenOdd(34)

"""

'''def total(numbers):
    total=0
    for k in numbers:
        total+=k
    return total
 

l=[34,12,4,7]
s=total(l)
print("Average :",s/len(l))'''

x=10
def add(a):
    global x
    x=x+a

add(2)

print(x)
