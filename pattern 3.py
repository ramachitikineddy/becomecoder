n=int(input())
for i in range(1,n+1):
    if i%2==1:
        for j in range(1,n+1):
            print(i,end=" " )
    else:
        for j in range(1,n+1):
            print(j,end=" ")
    print()
  """      
1 1 1 1 1 
1 2 3 4 5 
3 3 3 3 3 
1 2 3 4 5 
5 5 5 5 5 """
