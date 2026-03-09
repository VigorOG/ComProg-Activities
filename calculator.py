print("Calculator Menu")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

operation = input("Choose an operation (1-4): ")

first = float(input("Input the first value: "))
second = float(input("Input the second value: "))

answer = None
operator = ""

if operation == "1":
    answer = first + second
    operator = "+"
elif operation == "2":
    answer = first - second
    operator = "-"
elif operation == "3":
    answer = first * second
    operator = "*"
elif operation == "4":
    operator = "/"
    if second == 0:
        print("Error: Division by zero is not allowed.")
    else:
        answer = first / second
else:
    print("Invalid option selected.")

if answer is not None:
    print("Result:", first, operator, second, "=", answer)