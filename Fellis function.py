n=int(input())
def f(n):
    if(n==1):
        return 1
    if(n==0):
        return 1
    return (f(n-1)+7*f(n-2)+(n//4))%(10**9+7)
print(f(n))