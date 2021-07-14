import random,time
stDate=input("Enter start date strictly in MM/DD/YYYY format:\n")
try:
    stTime=time.mktime(time.strptime(stDate,'%m/%d/%Y'))
except:
    print('Enter Start Date in correct format\nQuiting Program')
    quit()
enDate=input("Enter end date strictly in MM/DD/YYYY format:\n")
try:
    enTime=time.mktime(time.strptime(enDate,'%m/%d/%Y'))
except:
    print('Enter End Date in correct format\nQuiting Program')
    quit()
pTime=stTime+(random.random())*(enTime-stTime)
if(enTime<stTime):
    print('End Date should be greater than Starting Date')
    quit()
print(f'Printing random date between {stDate} and {enDate}')
print(time.strftime("%m/%d/%Y",time.localtime(pTime)))