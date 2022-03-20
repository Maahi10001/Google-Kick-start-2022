#solution of challenging nine
for j in range(int(input())):
    n=int(input())
    def sod(n):
        if(n==0):
            return 0
        if(n%9==0):
            return 9
        else:
            return(n%9)
    x=9-sod(n)
    s=str(n)
    ans=s+str(x)
    for i in range(0,len(s)):
        temp=s[0:i]+str(x)+s[i:len(s)]
        if(temp[0]=='0'):
            continue
        ans=min(temp,ans)
    print("Case #",j+1,": ",ans,sep="")