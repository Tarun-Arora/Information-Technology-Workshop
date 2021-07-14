x=[x for x in input("\nEnter the 4 digit comma separated binary numbers:\n").split(',')]
output=""
for i in x:
    if(len(i)==4):
        a=int(i[0])*8+int(i[1])*4+int(i[2])*2+int(i[3])
        if(a%5==0):
            output+=i+','
if(output!=""):
    print("The binary numbers divisible by 5 are: ",output[:-1])
else:
    print("None of the 4 digit binary numbers entered are divisible by 5")