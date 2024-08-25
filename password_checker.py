import re

def check_password_strength(password):
    # Criteria
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[\W_]', password) is not None  # Special characters

    # Count how many criteria are met
    strength_count = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])

    # Determine password strength
    if strength_count == 5:
        return "Very Strong"
    elif strength_count == 4:
        return "Strong"
    elif strength_count == 3:
        return "Moderate"
    elif strength_count == 2:
        return "Weak"
    else:
        return "Very Weak"

def get_feedback(password):
    feedback = []

    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    if not re.search(r'[A-Z]', password):
        feedback.append("Password should contain at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        feedback.append("Password should contain at least one lowercase letter.")
    if not re.search(r'[0-9]', password):
        feedback.append("Password should contain at least one digit.")
    if not re.search(r'[\W_]', password):
        feedback.append("Password should contain at least one special character (e.g., !@#$%^&*).")

    return feedback

def main():
    print("Password Complexity Checker")
    password = input("Enter your password: ")
    
    strength = check_password_strength(password)
    feedback = get_feedback(password)
    
    print(f"\nPassword Strength: {strength}")
    
    if feedback:
        print("\nSuggestions to improve your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")

if __name__ == "__main__":
    main()
