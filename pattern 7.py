n=int(input())
for i in range(1,n+1):
    if i%2==1:
        temp=1
    else:
        temp=0
    for j in range(1,n+1):
        print(temp,end=" ")
        if temp==0:
            temp=1
        else:
            temp=0
    print()
"""    
1 0 1 0 1 
0 1 0 1 0 
1 0 1 0 1 
0 1 0 1 0 
1 0 1 0 1 """
