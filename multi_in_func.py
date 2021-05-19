def mul(a,b,s=0):
    while a:
        if a%2:
            s=s+b
        a=a//2
        b=b*2
    return s
a,b=map(int,input().split())
s=mul(a,b)
print(s)


        
    
