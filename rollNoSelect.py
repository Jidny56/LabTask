import random

def read_student_ids(file_path):
    """
    Reads student IDs from a file and returns them as a list.
    
    Parameters:
    - file_path: Path to the text file containing student IDs, one per line.
    
    Returns:
    - A list of student IDs as strings.
    """
    try:
        with open(file_path, 'r') as file:
            student_ids = [line.strip() for line in file.readlines()]
        return student_ids
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except Exception as e:
        print(f"Error reading the file: {e}")
        return []

def select_random_student(students):
    """
    Selects a random student from the list, removes them, and returns the selected student.
    
    Parameters:
    - students: A list of student IDs.
    
    Returns:
    - The student ID of the selected student.
    """
    if not students:
        return None
    return students.pop(random.randint(0, len(students) - 1))

def main():
    # File path containing the student IDs
    file_path = 'student_ids.txt'
    
    # Read student IDs from the file
    students = read_student_ids(file_path)
    
    if not students:
        return
    
    # Counter for viva rounds
    viva_counter = 1
    
    # Loop to select students for viva
    while students:
        print(f"Viva #{viva_counter}:")
        
        # Randomly select a student
        selected_student = select_random_student(students)
        
        if selected_student:
            print(f"Student selected: {selected_student}")
        else:
            print("No students left to select.")
            break
        
        # Increment the viva round counter
        viva_counter += 1
    
    # All students have been selected, now reset the list
    print("\nAll students have been selected for viva.")
    print("Resetting the list to include all students again...\n")
    
    # Re-read the student IDs from the file to reset the list
    students = read_student_ids(file_path)
    
    # Optionally, shuffle students again if needed
    random.shuffle(students)

    # Restart the viva selection process if desired (or can be used for another run)
    print(f"\nViva #1 (after reset): {students[0]}")

if __name__ == "__main__":
    main()
