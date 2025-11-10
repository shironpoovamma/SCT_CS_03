import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    score = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        digit_criteria,
        special_char_criteria
    ])

    strength_levels = {
        5: "Very Strong ",
        4: "Strong ",
        3: "Moderate ",
        2: "Weak ⚠",
        1: "Very Weak ",
        0: "Extremely Weak "
    }

    feedback = []
    if not length_criteria:
        feedback.append("Use at least 8 characters.")
    if not uppercase_criteria:
        feedback.append("Add uppecase letters.")
    if not lowercase_criteria:
        feedback.append("Include lowercase letters.")
    if not digit_criteria:
        feedback.append("Include numbers.")
    if not special_char_criteria:
        feedback.append("Add special characters (e.g., !@#$%).")

    print(f"Password Strength: {strength_levels[score]}")
    if feedback:
        print("Suggestions to improve:")
        for tip in feedback:
            print(f"- {tip}")

# Example usage
password = input("Enter your password: ")
assess_password_strength(password)
