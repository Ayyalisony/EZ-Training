org="qwertyuiopasdfghjklzxcvbnm"
s=input()
ans=""
for i in org:
    if i not in s:
        ans=ans+i
print(ans)        