def harshad_num(n):
    t=n
    s=0
    while t:
        r=t%10
        t=t//10
        s=s+r
    if n%s==0:
        return True
    return False
n=int(input())
print(harshad_num(n))
        
