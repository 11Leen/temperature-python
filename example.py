#import random

#secret_number = random.randint(1, 20)
#attempts = 5
#print("I chose a number between 1 and 20, try to guess it ")

#while attempts > 0:
#    guess = int(input("enter your guess:"))
#    if guess == secret_number:
#        print("good, your right 🎉.")
#        break
        
#    elif guess < secret_number:
#        print("num bigger than you guess")
        
#    else:
#        print("num smaller than your guess")
        
    # شايف الفراغ اللي قبل الأسطر هاي تحت؟ هاد اللي لازم تعمله بالـ Tab:
#    attempts -= 1
#    print("remaining attempts", attempts)
    
#    if attempts == 0:
#        print("The attempts have ended! The correct number was:", secret_number)
        
#    play_again = input("do you want to play again? (yes/no):")
#    if play_again.lower() != "yes":
#        print("good buy! 👋")
#        break

#************************************************************************************

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

results = []  

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

    try:
        choice = int(input("Enter option number: "))
    except ValueError:
        print("Invalid input")
        continue

    if choice == 1:
        c = float(input("Enter the temperature in Celsius: "))
        res = c_to_f(c)
        print("result:", res, "°F")
        results.append(f"{c} °C → {res} °F")
    elif choice == 2:
        f = float(input("Enter the temperature in Fahrenheit: "))
        res = f_to_c(f)
        print("result:", res, "°C")
        results.append(f"{f} °F → {res} °C")
    elif choice == 3:
        c = float(input("Enter the temperature in Celsius: "))
        res = c_to_k(c)
        print("result:", res, "K")
        results.append(f"{c} °C → {res} K")
    elif choice == 4:
        k = float(input("Enter the temperature in Kelvin: "))
        res = k_to_c(k)
        print("result:", res, "°C")
        results.append(f"{k} K → {res} °C")
    elif choice == 5:
        f = float(input("Enter the temperature in Fahrenheit: "))
        res = f_to_k(f)
        print("result:", res, "K")
        results.append(f"{f} °F → {res} K")
    elif choice == 6:
        k = float(input("Enter the temperature in Kelvin: "))
        res = k_to_f(k)
        print("result:", res, "°F")
        results.append(f"{k} K → {res} °F")
    elif choice == 7:
        temps = input("Enter Celsius temperatures separated by commas: ")
        c_list = [float(x.strip()) for x in temps.split(",")]
        print("Converted list:")
        for c in c_list:
            res = c_to_f(c)
            print(c, "°C →", res, "°F")
            results.append(f"{c} °C → {res} °F")
    elif choice == 8:
        print("finish")
        print("\n--- All results ---")
        for r in results:
            print(r)
        break
    else:
        print("False choice")

    re_calculation = input("do you want to Recalculation? (Yes/No): ")
    if re_calculation.lower() != "yes":
        print("good bye! 👋")
        print("\n--- All results ---")
        for r in results:
            print(r)
        break
