# Program: Conditional Statements Demo (Menu-Driven)

def positive_negative_zero():
    n = int(input("Enter any number: "))
    if n > 0:
        print("It is a Positive number.")
    elif n < 0:
        print("It is a Negative number.")
    else:
        print("The number is Zero.")

def even_or_odd():
    n = int(input("Enter a number to check: "))
    if n % 2 == 0:
        print(f"{n} is an Even number.")
    else:
        print(f"{n} is an Odd number.")

def largest_among_three():
    x = int(input("Enter first value: "))
    y = int(input("Enter second value: "))
    z = int(input("Enter third value: "))
    if x >= y and x >= z:
        print("The biggest number is:", x)
    elif y >= x and y >= z:
        print("The biggest number is:", y)
    else:
        print("The biggest number is:", z)

def grade_from_marks():
    score = int(input("Enter your marks: "))
    if score >= 90:
        print("You got Grade: A")
    elif score >= 75:
        print("You got Grade: B")
    elif score >= 50:
        print("You got Grade: C")
    else:
        print("You have Failed.")

# Menu
while True:
    print("\n--- Conditional Statements Menu ---")
    print("1. Check Positive / Negative / Zero")
    print("2. Check Even / Odd")
    print("3. Find Largest Number (among 3)")
    print("4. Get Grade from Marks")
    print("5. Quit")
    
    ch = input("Choose an option (1-5): ")
    
    if ch == "1":
        positive_negative_zero()
    elif ch == "2":
        even_or_odd()
    elif ch == "3":
        largest_among_three()
    elif ch == "4":
        grade_from_marks()
    elif ch == "5":
        print("Thanks for using this program!")
        break
    else:
        print("Wrong input! Please select from 1 to 5.")
