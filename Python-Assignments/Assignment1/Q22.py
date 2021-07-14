a=[int(x) for x in input('Enter a list of Integers: ').split()]
s=""
for i in a:
    s+=str(i)
num=int(s)
print('Resultant Integer:',num)