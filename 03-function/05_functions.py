# ==========================================
# TOPIC: Functions in Python
# ==========================================

# A function is a reusable block of code designed to perform a specific task.
# Instead of writing the same code repeatedly, you define it once 
# and call it whenever you need it.


# ==========================================
# 1. Defining and Calling a Basic Function
# ==========================================
# Use the 'def' keyword followed by the function name and parentheses ().

def say_hello():
    print("Hello, welcome to Python functions! 👋")

print("--- 1. Basic Function Call ---")
say_hello()
say_hello()  # You can call it multiple times easily!
print()


# ==========================================
# 2. Functions with Parameters and Arguments
# ==========================================
# Parameters are placeholders in the definition; arguments are the actual values passed in.

def greet_user(name, language):
    print(f"Hello {name}! It's great that you are learning {language}. 🚀")

print("--- 2. Parameters & Arguments ---")
greet_user("Divyansh", "Python")
greet_user("Alex", "JavaScript")
print()


# ==========================================
# 3. The 'return' Statement
# ==========================================
# Functions can process data and send a result back using 'return'.

def calculate_rectangle_area(length, width):
    area = length * width
    return area  # Sends the calculated result back

print("--- 3. Return Values ---")
room_area = calculate_rectangle_area(12.5, 8.0)
print(f"The area of the room is: {room_area} sq meters\n")


# ==========================================
# 4. Default Parameters
# ==========================================
# You can assign default values to parameters in case an argument isn't provided.

def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}. 🐾")

print("--- 4. Default Parameters ---")
describe_pet("Buddy")             # Uses default animal_type ("dog")
describe_pet("Whiskers", "cat")    # Overrides default animal_type
print()


# ==========================================
# 5. Practical Mini-Project: Temperature Converter
# ==========================================

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print("--- 5. Temperature Converter ---")
c_temp = float(input("Enter temperature in Celsius (°C): "))
f_temp = celsius_to_fahrenheit(c_temp)
print(f"{c_temp}°C is equal to {round(f_temp, 2)}°F 🌡️")