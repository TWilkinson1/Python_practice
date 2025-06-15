# Simple Calculator Program
while True:
    operators = input("Enter an operator (+, -, *, /): ")
    if operators not in ("+", "-", "*", "/"):
        print("Invalid operator. Please enter one of +, -, *, /.")
        continue
    else:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    if operators == "+":
            result = num1 + num2
    elif operators == "-":
            result = num1 - num2
    elif operators == "*":
            result = num1 * num2
    elif operators == "/":
            result = num1 / num2
    print(f"The result of {num1} {operators} {num2} is: {result}")

    play_again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thank you for using the calculator. Goodbye!")
        break

