import copy

a=[[12,5,2],[8,"Ebin"]]

b=copy.copy(a)

b[0][1]="Python"

print(a[0])