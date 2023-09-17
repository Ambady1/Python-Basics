percentage = float(input("Enter your total mark percentage: "))

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 50:
    grade = "E"
else:
    grade = "Failed"

# Print the grade
print(f"Your grade is: {grade}")
