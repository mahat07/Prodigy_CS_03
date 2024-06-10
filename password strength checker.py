import re
def password_strength(password):
    # Initialize criteria counts
    length = len(password)
    upper = len(re.findall(r'[A-Z]', password))
    lower = len(re.findall(r'[a-z]', password))
    digits = len(re.findall(r'\d', password))
    special = len(re.findall(r'[^A-Za-z0-9]', password))

    # Assess the strength
    strength_points = 0
    feedback = []

    # Check length
    if length >= 8:
        strength_points += 2
        feedback.append("Good length (8 or more characters)")
    else:
        feedback.append("Too short (less than 8 characters)")

    # Check for uppercase letters
    if upper > 0:
        strength_points += 1
        feedback.append("Contains uppercase letters")
    else:
        feedback.append("Add atleast 1 uppercase letter")

    # Check for digits
    if digits > 0:
        strength_points += 1
        feedback.append("Contains digits")
    else:
        feedback.append("Add atleast one digit")

    # Check for special characters
    if special > 0:
        strength_points += 1
        feedback.append("Contains special characters")
    else:
        feedback.append("Add atleast 1 special character")

    # Determine strength level
    if strength_points <= 2:
        strength = "Weak"
    elif strength_points == 3:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback

def main():
    password = input("Enter your password: ")
    strength, feedback = password_strength(password)
    print(f"Password Strength: {strength}")
    print("Feedback:")
    for f in feedback:
        print(f"- {f}")

if __name__ == "__main__":
    main()
