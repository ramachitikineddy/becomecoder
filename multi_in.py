def mul(a,b,res=0):
    while a:
        if a%2:
            s=s+b
        a=a//2
        b=b*2
    return res
a,b=map(int,input().split())
res=mul(a,b)
print(res)

        
    
