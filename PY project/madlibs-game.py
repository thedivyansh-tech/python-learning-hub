# --- STEP 1: Ask the user for words ---
print("Welcome to Mad Libs!")
print("Fill in the blanks below:\n")

adjective = input("Enter an adjective (describing word, e.g., funny, giant): ")
animal = input("Enter an animal: ")
food = input("Enter a type of food: ")
verb = input("Enter an action verb (e.g., jump, dance): ")
place = input("Enter a place: ")


# --- STEP 2: Combine the words into a story ---
story = f"""
--- MY CRAZY DAY ---
One day, I saw a {adjective} {animal} eating a huge bowl of {food}.
Suddenly, it stood up and decided to {verb} all the way to {place}!
It was the funniest thing I have ever seen.
"""


# --- STEP 3: Display the final story ---
print(story)