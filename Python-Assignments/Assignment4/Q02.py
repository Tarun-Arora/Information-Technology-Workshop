class HexToDec:
    def __init__(self):
        self.hex=input('Enter a hexadecimal number: ')
    def Dec(self):
        s=self.hex
        ans=0;j=1
        for i in s[::-1]:
            if i<='9':
                ans+=(ord(i)-48)*j
            else :
                ans+=(ord(i)-55)*j
            j*=16
        return ans

hex_num=HexToDec()
print(f'The binary of {hex_num.hex} is',hex_num.Dec())
