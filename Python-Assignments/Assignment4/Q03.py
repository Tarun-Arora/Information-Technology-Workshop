class check():
    def __init__(self,c1,c2):
        self.class1=c1
        self.class2=c2
    def result(self):
        if issubclass(self.class1,self.class2):
            print(f'Yes, {self.class1} is a subclass of {self.class2}')
        else:
            print(f'No, {self.class1} is not a subclass of {self.class2}')

class parent():
    pass

class child(parent):
    pass

check(child,parent).result()
check(parent,child).result()