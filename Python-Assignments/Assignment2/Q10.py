def makeBold(fn):
    def wrapped():
        return '\033[1m'+fn()+'\033[0m'
    return wrapped
def makeItalic(fn):
    def wrapped():
        return '\x1B[3m'+fn()+'\x1B[23m'
    return wrapped
def doUnderline(fn):
    def wrapped():
        return '\033[4m'+fn()+'\033[0m'
    return wrapped
@makeBold
@makeItalic
@doUnderline
def hello():
    s=input('Enter Text: ')
    return s
print(hello())