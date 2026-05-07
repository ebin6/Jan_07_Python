"""
    *
   **
  ***
 ****
*****


"""
rows=5
for r in range(1,rows+1):
    for space in range(rows-r):
        print(" ",end="")
    for start in range(r):
        print("*",end="") 
    print("")

"""
1
2 3 
4 5 6
7 8 9 10

"""
num=1
for row in range(1,5):
    for c in range(row):
        print(num,end=" ")
        num+=1
    print("")


"""
Sample Pattern

1
2 6
3 7 10
4 8 11 13
5 9 12 14 15

"""

"""
A
A B 
A B C 
A B C D

"""
n=65
for r in range(1,5):
    for ch in range(r):
        print(chr(n),end=" ")
        n+=1 
    print("")

"""
A
B C
D E F 
G H I J

"""