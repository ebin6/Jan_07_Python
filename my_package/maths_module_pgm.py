def is_even(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
    

def factorial(num):
    fact=1
    for k in range(1,num+1):
        fact*=k
    return fact