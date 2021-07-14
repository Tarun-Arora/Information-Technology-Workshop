from collections import Counter
print("Number of words in the file :\n",Counter(open('test.txt','r').read().split()),sep='')