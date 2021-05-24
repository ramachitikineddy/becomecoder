"""18import math as m
def pronic_num(num):
    m=int(m.sqrt(num))+1
    if num==(m-1)*m:
        return True
    return False
num=int(input())
print(pronic_num(num))"""

def ispronic(n):
    for i in range(n):
        print(i)
        if n==i*(i+1):
            return True
        return False
n=int(input())
print(ispronic(n))
    
    
