def sumList(l):
    sum=0
    for i in l:
        if type(i)==list:
            sum+=sumList(i)
        else:
            sum+=i
    return sum

print('The sum of elements is:',sumList([1, 2, [3,4], [5,6]]))