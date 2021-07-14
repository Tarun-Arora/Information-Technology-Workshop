import random
file=open('test.txt','r')
l=file.read().split('\n')
i=random.randint(0,len(l)-1)
print('A random line of the file is:',l[i],sep='\n')