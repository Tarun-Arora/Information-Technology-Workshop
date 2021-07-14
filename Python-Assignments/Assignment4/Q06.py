class string:
    def __init__(self,s):
        self.str1 = s
    def rev(self):
        list1=(self.str1).split()
        self.str1=' '.join([x[::-1] for x in list1])
st=string(input('Enter a string to be reversed: '))
st.rev()
print('The reversed string is:',st.str1)
