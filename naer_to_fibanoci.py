def gen_fib(num):
    if num==0 or num==1:
        return True
    a,b=0,1
    while True:
        c=a+b
        if c==num:
            return True
        if c>num:
            print(b,num,c)
            if num-b<=c-num:
                print(b,end=" ")
            if num-b>=c-num:
                print(c,end=" ")
        
            return False    
        a=b
        b=c
#T=int(input())
#for i in range(T):
num=int(input())
print(gen_fib(num))
 

