# ==========================================
# TOPIC: Loops in Python (for and while)
# ==========================================

# Loops are used to repeat a block of code multiple times automatically,
# saving you from writing repetitive code.


# ==========================================
# 1. The 'for' Loop
# ==========================================
# A 'for' loop is used for iterating over a sequence (like a list, string, or range).

print("--- Example 1: Iterating over a List ---")
languages = ["Python", "JavaScript", "C", "PHP", "MySQL"]
for lang in languages:
    print(f"I want to master: {lang}")
print()

print("--- Example 2: Iterating using range() ---")
# range(start, stop, step) - Note that 'stop' is exclusive.
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

print("\nEven numbers up to 10:")
for i in range(2, 11, 2):
    print(i)
print()


# ==========================================
# 2. The 'while' Loop
# ==========================================
# A 'while' loop repeats a block of code AS LONG AS a specified condition is True.

print("--- Example 3: Basic While Loop (Countdown) ---")
countdown = 3
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1  # Crucial: update the condition variable to avoid an infinite loop!
print("Liftoff! 🚀\n")


# ==========================================
# 3. Loop Control Statements (break & continue)
# ==========================================

# break: Completely exits/stops the loop early.
print("--- Example 4: Using 'break' ---")
print("Searching for the number 3...")
for number in range(1, 10):
    if number == 3:
        print("Found 3! Stopping loop.")
        break
    print(f"Checked number: {number}")
print()

# continue: Skips the current iteration and moves to the next one.
print("--- Example 5: Using 'continue' ---")
print("Printing odd numbers between 1 and 6:")
for num in range(1, 7):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)
print()


# ==========================================
# 4. Practical Mini-Project: Multiplication Table
# ==========================================
print("--- Example 6: Dynamic Multiplication Table ---")
num = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    product = num * i
    print(f"{num} x {i} = {product}")