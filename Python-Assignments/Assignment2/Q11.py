def h_sum(n):
    s=0
    for i in range(1,n):
        s+=1/i
    return s
n=int(input('Enter the value of n: '))
print(h_sum(n))
