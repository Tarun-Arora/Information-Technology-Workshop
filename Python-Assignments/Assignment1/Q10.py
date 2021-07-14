s=input("\nEnter the string: ")
lower=0;upper=0
for i in s:
    if(ord(i)>=65 and ord(i)<92):
        upper+=1
    elif (ord(i)>=97 and ord(i)<123):
        lower+=1
print("No. of Upper case characters :",upper)
print("No. of Lower case Characters :",lower)