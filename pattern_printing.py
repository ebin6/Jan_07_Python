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

