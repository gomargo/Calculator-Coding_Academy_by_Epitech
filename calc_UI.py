import time
from calc import Calc

cal = Calc()

# Banner logo because branding is important
print("")
print("")
print(" .d888b.         88               88        88")
print(" d8P  Y8b        88               88        88")
print(" 88    88        88               88        88")
print(" 88       8888b. 88 .d88b 88   88 88  888b. 88888 .d8b.  888d888")
print(" 88           8b 88 d8P   88   88 88     8b 88    d8 88b 88P   ")
print(" 88    88 .d8888 88 88    88   88 88 .d8888 88    88  88 888")
print(" Y8b  d8P 88  88 88 Y8b.   Y8b 88 88 88  88 Y8b.  Y8..8P 888")
print("   Y88P    Y8888 88  Y88P   Y8888 88 Y88888   Y88  Y8P   888")
print("  .d88b.    .d88b.   .d88b.   .d88b.")
print(" d8P  Y8b  d8P  Y8b d8P  Y8b d8P  Y8b")
print("        88 88    88 88    88 88    88 ")
print("      .d8P 88    88 88    88 88    88 ")
print("  .od88P   88    88 88    88 88    88 ")
print(" d8P       88    88 88    88 88    88 ")
print(" 88        Y8b  d8P Y8b  d8P Y8b  d8P ")
print(" 88888888    Y88P     Y88P     Y88P")
print("")

def menu():
    print("")
    print("#"*60)
    print("#")
    print("# CHOOSE AN OPERATION")
    print("#")
    print("# 1. Addition \t\t\t 12: Sine in Degrees")
    print("# 2. Substraction \t\t 13: Cosine in Degrees")
    print("# 3. Multiplication \t\t 14: Tan in Degrees")
    print("# 4. Division \t\t\t 15: Cosecant in Degrees")
    print("# 5. Sine in Radians \t\t 16: Secant in Degrees")
    print("# 6. Cosine in Radians \t\t 17: Cot in Degrees")
    print("# 7. Tan in Radians \t\t 18: Natural Log")
    print("# 8. Cosecant in Radians \t 19: Base 10 log")
    print("# 9. Secant in Radians \t\t 20: Log Base 'x'")
    print("# 10. Cot in Radians \t\t 21: Square Root")
    print("# 11. Pi \t\t\t 22: Power Of")
    print("#")
    print("# "+"-"*57)
    print("#")
    print("# 0. Exit the Program")
    print("#")
    print("#"*60)
    print("")

def exception():
    print("")
    print("#"*60)
    print("#")
    print("# Please enter a valid number")
    print("#")
    print("#"*60)
    print("")
    time.sleep(2)
    menu()

menu()

choice = ""

while True:
    try:
        choice = int(input("Enter a number: "))
        print("")
    except:
        print("")
        print("#"*60)
        print("#")
        print("# Please choose between the offered options (0 to 22)")
        print("#")
        print("#"*60)
        print("")
        time.sleep(2)
        menu()
    if choice == 0:
        print("")
        print("#"*60)
        print("#")
        print("# You are closing Calculator 2000. See you soon!")
        print("#")
        print("#"*60)
        print("")
        exit()
    elif choice == 1:
        try:
            a = float(input("Enter your 1st number to add: "))
            b = float(input("Enter your 2nd number to add: "))
            cal.add(a,b)
            time.sleep(2)
            menu()
        except:
            exception()
    elif choice == 2:
        try:
            a = float(input("Enter your 1st number to substract: "))
            b = float(input("Enter your 2nd number to substract: "))
            cal.substract(a,b)
            time.sleep(2)
            menu()
        except:
            exception()
    elif choice == 3:
        try:
            a = float(input("Enter your 1st number to multiply: "))
            b = float(input("Enter your 2nd number to multiply: "))
            cal.multiply(a,b)
            time.sleep(2)
            menu()
        except:
            exception()
    elif choice == 4:
        try:
            a = float(input("Enter your 1st number to divide: "))
            b = float(input("Enter your 2nd number to divide: "))
            cal.divide(a,b)
            time.sleep(2)
            menu()
        except:
            exception()
    elif choice == 5:
        try:
            a = float(input("Enter a number to find its Sine in Radians: "))
            cal._sin(a)
            time.sleep(2)
            menu()
        except:
            exception()
    elif choice == 6:
        try:
            a = float(input("Enter a number to find its Cosine in Radians: "))
            cal._cos(a)
            time.sleep(2)
            menu()
        except:
            exception()
    elif choice == 7:
        try:
            a = float(input("Enter a number to find its Tan in Radians: "))
            cal._tan(a)
            time.sleep(2)
            menu()
        except:
            exception()
    elif choice == 8:
        try:
            a = float(input("Enter a number to find its Cosecant in Radians: "))
            cal.cosecrad(a)
            time.sleep(2)
            menu()
        except:
            exception()
    elif choice == 9:
        try:
            a = float(input("Enter a number to fnd its Secant in Radians: "))
            cal.secrad(a)
            time.sleep(2)
            menu()
        except:
            exception()
    elif choice == 10:
        try:
            a = float(input("Enter a number to find its Cot in Radians: "))
            cal.cotrad(a)
            time.sleep(2)
            menu()
        except:
            exception()
    elif choice == 11:
        cal._pi()
    elif choice == 12:
        try:
            a = float(input("Enter a number to find its Sine in Degrees: "))
            cal.sindeg(a)
            time.sleep(2)
            menu()
        except:
            exception()
    elif choice == 13:
        try:
            a = float(input("Enter a number to find its Cosine in Degrees: "))
            cal.cosdeg(a)
            time.sleep(2)
            menu()
        except:
            exception()
    elif choice == 14:
        try:
            a = float(input("Enter a number to find its Tan in Degrees: "))
            cal.tandeg(a)
            time.sleep(2)
            menu()
        except:
            exception()
    elif choice == 15:
        try:
            a = float(input("Enter a number to find its Cosecant in Degrees: "))
            cal.cosecdeg(a)
            time.sleep(2)
            menu()
        except:
            exception()
    elif choice == 16:
        try:
            a = float(input("Enter a number to find its Secant in Degrees: "))
            cal.secdeg(a)
            time.sleep(2)
            menu()
        except:
            exception()
    elif choice == 17:
        try:
            a = float(input("Enter a number to find its Cot in Degrees: "))
            cal.cotdeg(a)
            time.sleep(2)
            menu()
        except:
            exception()
    elif choice == 18:
        try:
            a = float(input("Enter a number to find its Natural Log: "))
            cal.ln(a)
            time.sleep(2)
            menu()
        except:
            exception()
    elif choice == 19:
        try:
            a = float(input("Enter a number to find its Base 10 log: "))
            cal.lnten(a)
            time.sleep(2)
            menu()
        except:
            exception()
    elif choice == 20:
        try:
            a = float(input("Enter a base number: "))
            x = float(input("Enter a number to find its log to the given log value: "))
            cal.lnbasex(a,x)
            time.sleep(2)
            menu()
        except:
            exception()
    elif choice == 21:
        try:
            a = float(input("Enter a number to find its Square Root: "))
            cal.lnten(a)
            time.sleep(2)
            menu()
        except:
            exception()
    elif choice == 22:
        try:
            a = float(input("Enter a number: "))
            b = float(input("Enter its power: "))
            cal.powerOf(a,b )
            time.sleep(2)
            menu()
        except:
            exception()