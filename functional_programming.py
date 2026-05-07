numbers=[12,45,2,7]

l=list(filter(lambda num:num%2==0,numbers))

print(l)

from functools import reduce

fact=reduce(lambda a,b:a*b,range(1,6))
print(fact)