def bou_fib(l,u,a=0,b=1):
    c=0
    while c<=u:
        c=a+b
        if c>=l and c<=u:
            print(c,end=" ")
        
        a=b
        b=c
l,u=map(int,input().split())
bou_fib(l,u)
        
