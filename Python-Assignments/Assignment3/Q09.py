file=open('test.txt','w')
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
file.write('\n'.join(color))
file.close()