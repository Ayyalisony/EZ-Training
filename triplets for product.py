n=input()
a=list(map(int,input().split()))
pro=1
t=60
c=0
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        for k in range(j+1,len(a)):
            print("indexes",i,j,k)
            print("values",a[i],a[j],a[k])
            pro=a[i]*a[j]*a[k]
            if pro==t:
                print(pro)
                print("triplet",a[i],a[j],a[k])
                c=c+1
        print() 
print(c)        