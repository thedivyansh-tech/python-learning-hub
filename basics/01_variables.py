# ==========================================
# TOPIC 1: Variables and Data Types in Python
# ==========================================

# 1. What is a Variable?
# A variable is a container used to store data values. 
# You don't need to declare a variable's type ahead of time; 
# Python automatically figures it out based on the value you assign using (=).

message = "Hello, Python learner!"
print(message)


# 2. Core Data Types in Python
# Python has several built-in data types. Here are the four most common ones:

# String (str): Used for text, enclosed in single or double quotes.
name = "Alice"

# Integer (int): Used for whole numbers (positive or negative).
age = 25

# Float (float): Used for numbers with decimal points.
price = 19.99

# Boolean (bool): Represents truth values -> True or False.
is_online = True


# 3. Printing Variables and Checking Types
# You can use the print() function to display information, 
# and the type() function to check what data type a variable holds.

print("--- Data Types Demonstration ---")
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Price:", price, "| Type:", type(price))
print("Is Online?", is_online, "| Type:", type(is_online))


# 4. Variable Reassignment
# Variables can change their values while your program runs.

score = 50        # score starts as an integer
print("\nInitial score:", score)

score = 100       # score gets updated
print("Updated score:", score)


# 5. Rules for Naming Variables:
# - Must start with a letter or an underscore (_).
# - Cannot start with a number.
# - Case-sensitive (my_variable and My_Variable are two different things).
# - Use 'snake_case' for multi-word variables (e.g., total_score instead of totalscore).

user_age = 30
total_items = 5
_hidden_variable = "Secret"