# Q7. Set & Dictionary Operations:
# Create set with 6 students including duplicates
# Print set
# Add 2 new students
# Create dictionary of 4 students with marks
# Print:
# Distinction for marks >= 75
# Pass for marks >= 60
# Fail otherwise

def set_and_dictionary_operations() -> None:
    
    print("--- 1. Set Operations ---")
    
    
    student_list_with_duplicates = ["Alice", "Bob", "Charlie", "Alice", "David", "Bob"]
    print(f"List of students with duplicates: {student_list_with_duplicates}")
    
   
    student_set = set(student_list_with_duplicates)
    print("Set of students (duplicates automatically removed):")
    print(student_set)
    print()
    
    
    student_set.add("Emma")
    student_set.add("Frank")
    print("Set of students after adding 'Emma' and 'Frank':")
    print(student_set)
    print("\n" + "-"*40 + "\n")

    print("--- 2. Dictionary Operations ---")
    
   
    student_marks = {
        "Alice": 82,
        "Bob": 58,
        "Charlie": 75,
        "David": 45
    }
    
    print("Student Marks Dictionary:")
    print(student_marks)
    print("\nGrade Results:")
    
    
    for student, marks in student_marks.items():
        if marks >= 75:
            grade = "Distinction"
        elif marks >= 60:
            grade = "Pass"
        else:
            grade = "Fail"
            
        print(f"Student: {student:<8} | Marks: {marks:<3} | Result: {grade}")



if __name__ == "__main__":
    print("--- Set & Dictionary Operations Test ---")
    set_and_dictionary_operations()
