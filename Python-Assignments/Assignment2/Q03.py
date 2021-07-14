def replace_with_sum(dic):
    dic['V+VI']=(dic['V']+dic['VI'])/2
    del dic['V'],dic['VI']
dic_list=[{'id' : 1, 'subject' : 'math', 'V' : 70, 'VI': 82},
{'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},{'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}]
for i in dic_list:
    replace_with_sum(i)
print(dic_list)