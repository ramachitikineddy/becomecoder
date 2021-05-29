n=int(input())
for i in range(n,0,-1):
    t=n
    for j in range(1,i+1):
        print(t,end=" ")
        t-=1
    print()
