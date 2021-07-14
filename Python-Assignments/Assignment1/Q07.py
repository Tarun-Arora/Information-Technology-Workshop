n=int(input("\nEnter number of lines of Pascal's Triangle to be printed: "))
for i in range(n):
    k=1
    print(" "*(n-1-i),end='')
    print(k,end=' ')
    for j in range(0,i):
        k=int((k*(i-j))/(j+1))
        print(k,end=' ')
    print('')