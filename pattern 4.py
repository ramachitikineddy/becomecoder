n=int(input())
for i in range(1,n+1):
        for j in range(1,n+1):
            if j==1:
                j=i
            print(j,end=" " )
        print()
  """      
1 2 3 4 5 
2 2 3 4 5 
3 2 3 4 5 
4 2 3 4 5 
5 2 3 4 5 """
