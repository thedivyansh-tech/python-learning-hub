# ==========================================
# TOPIC: Conditional Statements (if, elif, else)
# ==========================================

# Conditional statements allow your program to make decisions 
# based on whether certain conditions are True or False.


# 1. Basic if Statement
# Code inside the block only runs if the condition is True.
age = int(input("Enter your age: "))

if age >= 18:
    print("You are legally an adult.\n")


# 2. if-else Statement
# Handles both the True case and the alternative False case.
temperature = float(input("Enter the current temperature in °C: "))

if temperature > 30:
    print("It's a hot day outside! Stay hydrated. ☀️\n")
else:
    print("The weather is pleasant or cool. 🍃\n")


# 3. if-elif-else Statement (Multiple Conditions)
# Python checks conditions from top to bottom and runs the FIRST one that is True.
score = int(input("Enter your exam score (0-100): "))

if score >= 90:
    print("Grade: A (Outstanding!)\n")
elif score >= 80:
    print("Grade: B (Great job!)\n")
elif score >= 70:
    print("Grade: C (Good effort!)\n")
elif score >= 60:
    print("Grade: D (Needs improvement.)\n")
else:
    print("Grade: F (Failed, but you can try again!)\n")


# 4. Combining Conditions with Logical Operators (and, or, not)
print("--- Movie Ticket Discount Checker ---")
user_age = int(input("Enter your age for the ticket: "))
is_student_input = input("Are you a student? (yes/no): ").strip().lower()
has_student_id = (is_student_input == "yes")

# 'or' requires AT LEAST ONE condition to be True
# 'and' requires BOTH conditions to be True
if user_age < 12 or user_age >= 65:
    print("You qualify for the child/senior discount! 🎉")
elif user_age >= 18 and has_student_id:
    print("You qualify for the student discount! 🎓")
else:
    print("Standard ticket pricing applies. 🎟️")