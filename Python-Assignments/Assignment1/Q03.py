s=input("\nEnter a String: ")
posNot=s.find("not")
if(posNot!=-1):
    print("The first position of 'not' is at index",posNot)
else:
    print("The given string does not contain 'not'")

posPoor=s.find("poor")
if(posPoor!=-1):
    print("The first position of 'poor' is at index",posPoor)
else:
    print("The given string does not contain 'poor'")

if(posPoor!=-1 and posNot!=-1 and posPoor>posNot):
    print("Resultant String:",s[:posNot]+'good'+s[(posPoor+4):])
else:
    print('Resultant String:',s)