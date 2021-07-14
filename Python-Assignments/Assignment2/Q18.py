def reverse(s):
    ans=''
    for i in s:
        ans=i+ans
    return ans
s=input('Enter a string to be reversed:\n')
print('The reversed string is:\n',reverse(s),sep='')