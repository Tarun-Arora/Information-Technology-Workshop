file=open('test.txt','a+')
file.seek(0)
print('Input:',file.read())
file.writelines('\n'+input('Enter The Text You Want To Add to the file: '))
file.seek(0)
print('Output:',file.read())
file.close()