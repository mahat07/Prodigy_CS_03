The password_strength function calculates the password's strength based on the length and presence of different character types (uppercase, lowercase, digits, special characters).
It uses regular expressions to count the occurrences of each type of character.
Points are awarded based on whether the password meets each criterion.
Feedback:

Feedback is provided to the user for each criterion, indicating whether the password meets that criterion or not.
Strength Levels:

The strength is categorized into three levels: "Weak", "Moderate", and "Strong" based on the total points.
Main Function:

The main function prompts the user to enter a password, calls the password_strength function, and then prints the password strength and feedback.
How to Use
Run the script.
Enter a password when prompted.
The tool will output the password's strength and provide feedback on how it can be improved.
This simple tool can be enhanced further by adding more criteria, such as checking for common passwords, sequences, or using a dictionary to check against common words. For now, it covers basic criteria to help users create stronger passwords.
