#solution for interesting integers
def func(n):
    pro,su=1,0
    for z in str(n):
        pro*=int(z)
        su+=int(z)
    return pro%su==0
p=0
for i in range(int(input())):
    a,b=map(int,input().split())
    count=0
    for y in range(a,b+1):
        if func(y):
            count+=1
    print("Case #"+str(p+1)+":",count)
    p-=1
