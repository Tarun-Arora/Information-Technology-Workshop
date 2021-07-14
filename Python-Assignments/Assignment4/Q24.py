from matplotlib import pyplot as plt
x = [5, 3, 6, 4, 7, 1, 8, 9, 10, 4]
y = [2, 4, 5, 7, 6, 8, 9, 11, 12, 12]
val = int(input("Enter 1 for histogram, 2 for bar chart, 3 for line graph, 4 for scatter graph: "))
if val == 1:
    plt.xlabel('Value range')
    plt.ylabel('Frequency')
    plt.hist(x, 10, (0, 10), rwidth=0.5, color="red")
else:
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    if val == 2:
        plt.bar(x, y, width=0.5, color=["red", "black"])
    elif val == 3:
        plt.plot(x, y)
    elif val == 4:
        plt.scatter(x, y)
plt.show()