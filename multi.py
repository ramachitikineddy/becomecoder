a,b=map(int,input().split())
s=0
while a:
    if a%2:
        s=s+b
    a=a//2
    b=b*2
print(s)
        
    
