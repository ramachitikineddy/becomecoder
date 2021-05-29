n=int(input())
for i in range(0,n+1):
    for s in range(0,i):
        print(" ",end="")
    for j in range(n,i,-1):
        print('*',end="")
    print()
 """   
*****
 ****
  ***
   **
    *"""
