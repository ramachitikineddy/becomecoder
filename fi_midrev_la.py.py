num=int(input())
nn=0
temp=num
f=0
l=0
c=r=0
k=0
p=1
while num:
    r=num%10
    num=num//10
    c+=1
num=temp#123
k=c=c-1#2
if num>0:
    l=num%10#3
    f=num//pow(10,c)#1
while num:
    r=num%10#3
    num=num//10#12
    if c==k:#2
         r=f#3=1
    elif c==0:
         r=l#1=3
    nn=nn*10+r#1*10+2=12*10+3=123
    c=c-1
print(nn)
