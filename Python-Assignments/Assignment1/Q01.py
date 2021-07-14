s=input('Enter a string: ')
k=len(s)
if(k<2):
    print('Empty String')
else:
    print(s[:2]+s[-2:])
