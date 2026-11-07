# Ask the user for their grade
grade = int(input("Enter your grade (0-100): "))

# Check the grade
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

# Print the result
print("Your grade is:", letter)

# Show a message based on the grade
message = "Congratulations!" if grade >= 70 else "Keep trying!"
print(message)