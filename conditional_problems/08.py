# Password Strength Checker

password = "admin123!@#"

length = len(password);
if length < 6:
    strength = "Weak"
elif length <= 10:
    strength = "Weak"
else:
    strength = "Strong"

print(f"Strength: {strength}")