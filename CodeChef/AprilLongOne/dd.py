def dd(n,a):
    s=sum(a)
    ans=0
    # print(s)
    i=1
    while(s>=0):
        ans+=1
        s-=i
        i+=1
    print(ans-1)
        
print(dd(4,[1,1,3,4]))