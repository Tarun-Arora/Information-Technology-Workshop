def merge(m,n):
    list=[]
    i=0;j=0
    while(i<len(m) and j<len(n)):
        if(m[i]>n[j]):
            list.append(n[j]);j+=1
        else:
            list.append(m[i]);i+=1
    while(j<len(n)):
        list.append(n[j]);j+=1
    while(i<len(m)):
        list.append(m[i]);i+=1
    return list
print("\nEnter the details of the two lists")
m=[int(x) for x in input("Enter all elements of first list: ").split(' ')]
n=[int(x) for x in input("Enter all elements of second list: ").split(' ')]
print("The two lists you enetered are",m,"and",n)
print("The resultant list is:",merge(m,n))