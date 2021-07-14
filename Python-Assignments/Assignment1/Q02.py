s=input('Enter a string: ')
ans=""
ans+=s[0]
for i in range (1,len(s)):
    if(s[i]==s[0]):
        ans+="$"
    else:
        ans+=s[i]
print(ans)