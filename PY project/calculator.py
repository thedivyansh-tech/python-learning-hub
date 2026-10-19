print("=== SIMPLE CALCULATOR ===")

# Step 1: Ask the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Ask the user what operation they want to do
print("\nChoose an operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("Enter your choice (1, 2, 3, or 4): ")

# Step 3: Perform the calculation based on their choice
if choice == "1":
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")

elif choice == "2":
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")

elif choice == "3":
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")

elif choice == "4":
    # Check if the user is trying to divide by zero
    if num2 == 0:
        print("\nError: Cannot divide by zero!")
    else:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")

else:
    print("\nInvalid choice! Please restart and pick 1, 2, 3, or 4.")