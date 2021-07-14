def sort_by_float(e):
    return float(e[1])
l=[('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
l.sort(reverse=True,key=sort_by_float)
print('Sorted List\n',l)