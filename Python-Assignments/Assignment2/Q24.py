import random
tickets=[]
while len(tickets)<100:
    a=random.randint(1000000000,9999999999)
    if a not in tickets:
        tickets.append(a)
lucky=[]
while len(lucky)<2:
    a=random.randint(0,99)
    if a not in lucky:
        lucky.append(a)
print('Creating 100 random lottery tickets')
print('Lucky 2 lottery tickets are',[tickets[lucky[0]],tickets[lucky[1]]])