class firstClass:
    data1='Default';data2='Values'

class emptyClass:
    pass

obj=firstClass()
print(f'Initial value, data1 = "{obj.data1}" and data2 = "{obj.data2}" .')
obj.data1,obj.data2=input('Enter new values of data1 and data2: ').split()
print(f'Final value, data1 = "{obj.data1}" and data2 = "{obj.data2}" .')
