class parent():
    def mem1(self):
        print('This member is accessed through parent class name')
    def mem2(self):
        print('This member is accessed through super')

class dummy(parent):
    def __init__(self):
        print('Dummy object created using Dummy class')
        parent.mem1(self)
        super().mem2()

a=dummy()