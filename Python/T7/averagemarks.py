def calculate_average(maths_marks, english_marks, science_marks, history_marks, geography_marks):
    """This function takes the marks in 5 subjects as inputs and returns the average marks"""
    # Calculate the sum of the marks
    total_marks = maths_marks + english_marks + science_marks + history_marks + geography_marks
    # Calculate the average marks by dividing the total marks by the number of subjects
    average_marks = total_marks / 5
    # Return the average marks
    return average_marks
# Prompt the user for their marks in each subject
maths_marks = float(input("Please enter your marks in Maths: "))
english_marks = float(input("Please enter your marks in English: "))
science_marks = float(input("Please enter your marks in Science: "))
history_marks = float(input("Please enter your marks in History: "))
geography_marks = float(input("Please enter your marks in Geography: "))
# Call the calculate_average() function and print the result
average_marks = calculate_average(maths_marks, english_marks, science_marks, history_marks,
geography_marks)
print(f"Your average marks are {average_marks:.2f}")
# The : character is used to separate the placeholder (average_marks) from the format specifier (.2f).