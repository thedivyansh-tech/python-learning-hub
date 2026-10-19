print("=== Welcome to My Password Checker ===")
password = input("Enter a password to check: ")
score = 0
print("\nRunning security checks...\n")
if len(password) >= 8:
    print("✅ Good! Password is at least 8 characters long.")
    score = score + 1
else:
    print("❌ Too short! Make it at least 8 characters.")
has_uppercase = False
has_lowercase = False
has_number = False
for char in password:
    if char.isupper():
        has_uppercase = True
    elif char.islower():
        has_lowercase = True
    elif char.isdigit():
        has_number = True
if has_uppercase:
    print("✅ Found an uppercase letter (A-Z).")
    score = score + 1
else:
    print("❌ Missing an uppercase letter (A-Z).")
if has_lowercase:
    print("✅ Found a lowercase letter (a-z).")
    score = score + 1
else:
    print("❌ Missing a lowercase letter (a-z).")
if has_number:
    print("✅ Found a number (0-9).")
    score = score + 1
else:
    print("❌ Missing a number (0-9).")
print("\n-----------------------------------")
print(f"Your final security score: {score} out of 4")
if score == 4:
    print("🎉 Strong Password! Your account is safe.")
elif score >= 2:
    print("⚠️ Medium Password. Try adding more variety to it.")
else:
    print("❌ Weak Password! Please try again with letters and numbers.")
    
    
    # python ".\PY project\password-checker.py" use this command to run this 