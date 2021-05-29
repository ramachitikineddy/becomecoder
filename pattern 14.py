n=int(input())
for i in range(n,0,-1):
    if i%2==1:
        for j in range(1,i+1):
            print(j,end=" ")
    else:
        t=i
        for j in range(1,i+1):
            print(t,end=" ")
            t-=1
    print()
"""
1 2 3 4 5 
4 3 2 1 
1 2 3 
2 1 
1 """
