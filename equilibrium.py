n=input()
a=list(map(int,input().split()))
for i in range(0,len(a)):
    f=0
    i1=i
    j=i+1
    s1=0
    s2=0
    while i>=0:
        s1+=a[i]
        i=i-1
    while j<len(a):
        s2+=a[j]
        j=j+1
    if s1==s2:
        print(i1+1)
        f=1
        break
if f==0:
    print(len(a)//2)
    
    