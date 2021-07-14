def insert_sting_middle(a,b):
    if(len(a)%2):
        print("Middle not found! String length is odd")
    else:
        k=int((len(a)/2))
        print("Resultant String:",a[:k]+b+a[k:])
        
a=input('Enter first string: ')
b=input('Enter string to be inserted: ')
insert_sting_middle(a,b)