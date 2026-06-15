def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

def c_to_k(celsius):
    return celsius + 273.15

def k_to_c(kelvin):
    return kelvin - 273.15

def f_to_k(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def k_to_f(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

while True:
    print("\n--- Temperature converter ---")
    print("1. from C to F ")
    print("2. from F to C")
    print("3. from C to K")
    print("4. from K to C")
    print("5. from F to K")
    print("6. from K to F")
    print("7. convert a list of Celsius to Fahrenheit")
    print("8. finish")

    choice = input("enter num:")

    if choice == "1":
        c = float(input("Enter the temperature in Celsius: "))
        print("result:", c_to_f(c), "°F")
    elif choice == "2":
        f = float(input("Enter the temperature in Fahrenheit: "))
        print("result:", f_to_c(f), "°C")
    elif choice == "3":
        c = float(input("Enter the temperature in Celsius: "))
        print("result:", c_to_k(c), "K")
    elif choice == "4":
        k = float(input("Enter the temperature in Kelvin: "))
        print("result:", k_to_c(k), "°C")
    elif choice == "5":
        f = float(input("Enter the temperature in Fahrenheit: "))
        print("result:", f_to_k(f), "K")
    elif choice == "6":
        k = float(input("Enter the temperature in Kelvin: "))
        print("result:", k_to_f(k), "°F")
    elif choice == "7":
        temps = input("Enter Celsius temperatures separated by commas: ")
        c_list = [float(x.strip()) for x in temps.split(",")]
        print("Converted list:")
        for c in c_list:
            print(c, "°C →", c_to_f(c), "°F")
    elif choice == "8":
        print("finish")
        break
    else:
        print("False choice")

    re_calculation = input("do you want to Recalculation? (Yes/No): ")
    if re_calculation.lower() != "yes":
        print("good bye! 👋")
        break
