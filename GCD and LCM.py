a=int(input())
b=int(input())
while b!=0:
    temp=a
    a=b
    b=b%temp
print(a) 
lcm=a*b//a
print(lcm)   
    