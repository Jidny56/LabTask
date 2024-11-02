import random

# Function to select random roll numbers
def select_random_students(filename, n=10):
    with open(filename, 'r') as file:
        roll_numbers = file.read().splitlines()
    return random.sample(roll_numbers, n)

# Use the function to select 10 students
selected_students = select_random_students('student_roll_numbers.txt')
print(selected_students)
