import os,shutil
print("My Current Working Directory: ",os.getcwd())
currdir=os.getcwd()
folder=input('Enter the name of new directory: ')
#Creating New Directory
new=currdir+"/"+folder
os.mkdir(new)
os.chdir(new)
f=open("myfile.txt","w+")
f.write('its myfile.txt')
f.seek(0)
print(f.read())
f.close()
shutil.rmtree(new)