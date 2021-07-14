letters=[0]*256
s=input("Enter a string: ")
for i in s:
    letters[ord(i)]+=1
for i in range(256):
    if(letters[i]>1):    
        print(chr(i),letters[i])