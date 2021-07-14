import random,string
def generate_password():
    s="";charac=0;lett=0;dig=0
    for i in range(10):
        if i>6:
            if lett==0:
                s+=string.ascii_letters[random.randint(0,51)];lett=1;continue
            elif charac==0:
                s+=string.punctuation[random.randint(0,31)];charac=1;continue
            elif dig==0:
                s+=string.digits[random.randint(0,9)];dig=1;continue
        c=chr(random.randint(33,126))
        if c in string.ascii_letters:
            lett+=1
        if c in string.punctuation:
            charac+=1
        if c in string.digits:
            dig+=1
        s+=c
    return s
print(f"First Random String: ${generate_password()}\nSecond Random String: ${generate_password()}\nThird Random String: ${generate_password()}")