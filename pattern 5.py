n=int(input())
for i in range(1,n+1):
    if i%2==0:
        for j in range(1,n+1):
            print(i,end=" " )
    else:
        for j in range(n,0,-1):
            print(j,end=" ")
    print()
 """       
5 4 3 2 1 
2 2 2 2 2 
5 4 3 2 1 
4 4 4 4 4 
5 4 3 2 1 
>>> """
