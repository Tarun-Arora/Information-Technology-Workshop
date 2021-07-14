file=open('test.txt','r')
print('Number of lines in the file:',len(file.read().split('\n')))
file.close() 