def is_disarium(n):
    pos=0
    t=n
    s=0
    while t:
        t=t//10
        pos+=1
    while n:
        r=n%10
        n=n//10
        s=s+pow(r,pos)
        pos-=1
    return s
n=int(input())
print(is_disarium(n)==n)
        
