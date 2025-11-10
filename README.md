Password Strength Checker
Overview
This Python program evaluates the strength of a user-provided password based on five key criteria:
 Minimum length (at least 8 characters)
 Presence of uppercase letters
 Presence of lowercase letters
 Inclusion of numeric digits
 Use of special characters (e.g., !@#$%^&*())
It assigns a score from 0 to 5 and categorizes the password as Extremely Weak, Very Weak, Weak, Moderate, Strong, or Very Strong. If the password does not meet all criteria, the program provides actionable suggestions to improve its strength.
Features
 Real-time password strength assessment
 Clear feedback and improvement tips
 Easy to integrate into larger applications or GUIs
Usage
 Run the script in a Python environment.
 Enter a password when prompted.
 View the strength rating and suggestions.
Example
Enter your password: MyPass123
Password Strength: Strong (4/5)
Suggestions to improve:
 Add special characters (e.g., !@#$%)
Requirements
 Python 3.x
 re module (standard library)
