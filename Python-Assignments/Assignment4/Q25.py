def error_handling(a, b):
    try:
        a = int(a)
        b = int(b)
        if a == b:
            raise ZeroDivisionError()
        else:
            n = (a + b) / (a - b)
    except ValueError:
        return "Integer values required."
    except ZeroDivisionError:
        return "Value of a and b should not be equal !"
    else:
        return n
    finally:
        print("Process complete")
a, b = [x for x in input("Enter the value of a and b: ").split()]
print('Result of (a+b)/(a-b)\n',error_handling(a, b))