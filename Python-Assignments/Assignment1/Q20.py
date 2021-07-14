list1=["red", "orange", "green", "blue", "white"]
list2=["black", "yellow", "green", "blue"]
ans1=[];ans2=[]
for i in list1:
    if i not in list2:
        ans1.append(i) 
for i in list2:
    if i not in list1:
        ans2.append(i)
print('\nGiven Lists:',list1,list2,sep='\n')
print("Color1-Color2:",ans1) 
print("Color2-Color1:",ans2) 