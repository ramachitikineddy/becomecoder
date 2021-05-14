#program to count max and min terms ina num
#byusing two loops
num=int(input())#123424
ma=num%10#4
mi=num%10#4
mac=0
mic=0
t=num
while num:
    r=num%10#4
    num=num//10#12342
    if r>ma:
        ma=r
        mac=1
    elif r<mi:
        mi=r
        mic=1
num=t
while num:
    r=num%10#4
    num=num//10
    if ma==r:
        mac+=1
    elif mi==r:
        mic+=1
print(ma,mi,mac,mic)
