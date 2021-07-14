import os

class decorator:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\x1B[3m'
    NORMAL = '\033[0m'

item_names = ["Chicken Strips", "French Fries", "Hamburger", "Hotdog", "Large Drink", "Medium Drink", "Milk Shake", "Salad", "Small Drink"]
item_prices = [3.50, 2.50, 4.00, 3.50, 1.75, 1.50, 2.25, 3.75, 1.25]
print(decorator.BOLD + decorator.UNDERLINE + "MENU CALCULATOR" + decorator.NORMAL+'\n')

while True:
    print(decorator.BOLD + decorator.ITALIC + "MENU CARD" + decorator.NORMAL+'\n')
    for i in range(len(item_names)):
        print(f'{decorator.ITALIC}{i+1}. {item_names[i]} - ${item_prices[i]}{decorator.NORMAL}')
    print("")
    print(decorator.ITALIC + "Enter exit to terminate." + decorator.NORMAL+'\n')
    val = input("Enter your order: ")
    # print("")
    if val == 'exit':
        break
    v = [0]*9
    flag = 0
    for i in val:
        try:
            v[(int(i) - 1)]+=1
        except ValueError:
            flag = 1
            break
        if i=='0':
            flag=0.5;break
    if flag == 1:
        print("Please enter integer values to order. \n")
        x = input("Press enter to continue: ")
        continue
    if flag == 0.5:
        print("Some items ordered are not available in the menu. \n")
        x = input("Press enter to continue: ")
        continue
    c = 0
    print(decorator.BOLD + decorator.UNDERLINE + "ITEMS ORDERED" + decorator.NORMAL)
    for i in range(9):
        if v[i]==0:
            continue
        print(f"{decorator.ITALIC}{item_names[i]} : {v[i]}{decorator.NORMAL}")
        c+=item_prices[i]*v[i]
    print(f'\n{decorator.BOLD}Total Cost : ${c}{decorator.NORMAL}\n')
    x = input("Press enter to continue: ")
    os.system('cls' if os.name == 'nt' else 'clear')
