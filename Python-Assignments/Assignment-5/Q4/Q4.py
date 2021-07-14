import pandas
import os,subprocess

class decorator:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\x1B[3m'
    NORMAL = '\033[0m'

def add_contact():
    print(decorator.BOLD + decorator.UNDERLINE + "Enter the contact details." + decorator.NORMAL)
    name = input(decorator.ITALIC + "Enter Contact Name : " + decorator.NORMAL)
    try:
        v = df.loc[name]
    except KeyError:
        email = input(decorator.ITALIC + "Enter Contact Email I'd : " + decorator.NORMAL)
        phone = input(decorator.ITALIC + "Enter Contact Phone no. : " + decorator.NORMAL)
        n = name + "\t" + email + "\t" + phone + "\n"
        f = open('data.txt', 'a')
        f.write(n)
        f.close()
        print("Contact Successfully Created ! \n")

    else:
        print("Contact name already exists.")
        print("\n\n")
        add_contact()


def display_contact():
    if df.empty:
        print("No contact in address book.\n")
        return
    print(df)


def search_contact():
    df = pandas.read_csv('data.txt', sep="\t", index_col="Contact_name")
    if df.empty:
        print("Address book empty. No contact to search. \n")
        return
    name = input(decorator.ITALIC + "Enter Contact Name : " + decorator.NORMAL)
    try:
        v = df.loc[name]
        email = df.at[name, "Contact_email"]
        phone = int(df.at[name, "Contact_phone"])
        print(decorator.BOLD + decorator.UNDERLINE + "Contact details." + decorator.NORMAL + "\n")
        print(decorator.ITALIC + "Contact name : " + decorator.NORMAL + str(name))
        print(decorator.ITALIC + "Email I'd : " + decorator.NORMAL + str(email))
        print(decorator.ITALIC + "Phone no. : " + decorator.NORMAL + str(phone) + "\n")
    except KeyError:
        print("No contact with this name found ! \n")


def modify_contact():
    df = pandas.read_csv('data.txt', sep="\t", index_col="Contact_name")
    if df.empty:
        print("Address book empty. No contact to modify. \n")
        return
    name = input(decorator.ITALIC + "Enter contact name to be modified : " + decorator.NORMAL)
    try:
        v = df.loc[name]
        delete(name)
        name = input(decorator.ITALIC + "Enter Contact New Name : " + decorator.NORMAL)
        email = input(decorator.ITALIC + "Enter Contact New Email I'd : " + decorator.NORMAL)
        phone = input(decorator.ITALIC + "Enter Contact New Phone no. : " + decorator.NORMAL)
        n = name + "\t" + email + "\t" + phone + "\n"
        f = open('data.txt', 'a')
        f.write(n)
        f.close()
        print("Contact Details Successfully Modified ! \n")
    except KeyError:
        print("No contact with this name found ! \n")


def delete(name):
    f = open('data.txt', 'r')
    v = []
    for i in f.readlines():
        v.append(i)
    f.close()
    for i in range(len(v)):
        x = v[i].split("\t")
        if x[0] == name:
            v.pop(i)
            break
    f = open('data.txt', 'w')
    for i in v:
        f.write(i)
    f.close()


def delete_contact():
    df = pandas.read_csv('data.txt', sep="\t", index_col="Contact_name")
    if df.empty:
        print("Address book empty. No contact to modify. \n")
        return
    name = input(decorator.ITALIC + "Enter contact name to be deleted : " + decorator.NORMAL)
    try:
        v = df.loc[name]
        delete(name)
        print("\nContact successfully deleted.")
    except KeyError:
        print("No contact with this name ! \n")

def takeInput():
    return int(input("Enter a option : "))

val = None
while val != 0:
    print(decorator.ITALIC + decorator.UNDERLINE + decorator.BOLD + "Welcome to Address Book." + decorator.NORMAL)
    print("\n\tEnter 1 to add contact.\n\tEnter 2 to Display contacts.\n\tEnter 3 to delete contact.\n\tEnter 4 to modify contact.\n\tEnter 5 to search contact.\n\tEnter 0 to exit.\n")
    val = takeInput()
    df = pandas.read_csv('data.txt', sep="\t", index_col="Contact_name")

    if val == 1:
        add_contact()
        print()
    elif val == 2:
        display_contact()
        print("\n\n")
    elif val == 3:
        delete_contact()
        print("\n\n")
    elif val == 4:
        modify_contact()
        print("\n\n")
    elif val == 5:
        search_contact()
        print("\n\n")
    elif val == 0:
        print("EXIT !")
        break
    else: 
        print(decorator.ITALIC + decorator.UNDERLINE + decorator.BOLD + '\nEnter a Valid Option.\n' + decorator.NORMAL)
        continue

    x = input("Press enter to continue: ")
    os.system('clear' if os.name == 'posix' else 'cls')
