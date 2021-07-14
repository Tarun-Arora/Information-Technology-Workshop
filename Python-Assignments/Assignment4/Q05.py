class rect:
    def __init__(self,l,w):
        self.len=l
        self.wid=w
    def area(self):
        return self.len*self.wid

rectangle=rect(12,10)
print(f'Length of Rectangle = {rectangle.len}')
print(f'Breadth of Rectangle = {rectangle.wid}')
print(f'Area of rectangle = {rectangle.area()}')