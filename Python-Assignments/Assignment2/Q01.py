dict1={'key1':1,'key2':3,'key3':2}
dict2={'key1':1,'key2':2}
for i in dict1:
    if i in dict2 and dict1[i]==dict2[i]:
        print(f"{i}: {dict1[i]} is present in both x and y") 