# ==========================================
# TOPIC 2: User Input and Type Casting in Python
# ==========================================

# 1. The input() Function
# The input() function allows your program to receive text from the user.
# It pauses execution, waits for the user to type something, and presses Enter.

name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to Python.\n")


# 2. Important Rule: input() Always Returns a String
# Even if the user types a number, Python treats it as text (a string).

age_input = input("Enter your age: ")
print(f"You entered: {age_input}")
print(f"Data type of age_input: {type(age_input)}")  # Output will be <class 'str'>


# 3. Type Casting (Converting Data Types)
# Because input is a string, you cannot do math with it directly. 
# You must convert (cast) it into an integer (int) or decimal (float) first.

age = int(age_input)                # Converts string to integer
birth_year = 2026 - age             # Now math works properly!
print(f"Based on that, you were born around: {birth_year}\n")


# 4. Direct Type Casting
# You can also wrap the input() function directly in int() or float():

height_feet = float(input("Enter your height in feet (e.g., 5.8): "))
print(f"Your height is {height_feet} feet.\n")


# 5. Mini Practice: Simple Addition Calculator
# Let's put it together to see why type casting is crucial.

print("--- Simple Addition Calculator ---")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is: {sum_result}")