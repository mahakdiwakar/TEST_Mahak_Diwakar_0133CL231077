# Q9. Student JSON Database:
# Create list of 4 students
# Fields: name, age, city, course, marks
# Save to students.json using indent=4
# Read file back
# Print students with marks > 70
# Print total student count

import json
import os

def student_json_database() -> None:
    
    filename = "students.json"
    
    
    students = [
        {
            "name": "Priya sharma ",
            "age": 20,
            "city": "New York",
            "course": "Computer Science",
            "marks": 85.5
        },
        {
            "name": "anshika sharma ",
            "age": 22,
            "city": "Los Angeles",
            "course": "Mechanical Engineering",
            "marks": 64.0
        },
        {
            "name": "Rahul Verma ",
            "age": 21,
            "city": "Chicago",
            "course": "Physics",
            "marks": 78.0
        },
        {
            "name": "Sneha Kapoor ",
            "age": 19,
            "city": "Boston",
            "course": "Mathematics",
            "marks": 92.5
        }
    ]

    print("Step 1: Writing student data to 'students.json' with indent=4...")
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)
        print(f"Data saved successfully to {filename}.\n")
    except Exception as e:
        print(f"Error saving file: {e}")
        return

    
    print("Step 2: Reading 'students.json' back into memory...")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            loaded_students = json.load(file)
        print(f"Successfully loaded {len(loaded_students)} student records from JSON.\n")
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    
    print("Step 3: Finding and printing students with marks > 70:")
    print("=" * 60)
    print(f"{'Name':<18} | {'Age':<3} | {'City':<12} | {'Course':<20} | {'Marks':<5}")
    print("-" * 60)
    for student in loaded_students:
        if student["marks"] > 70:
            print(f"{student['name']:<18} | {student['age']:<3} | {student['city']:<12} | {student['course']:<20} | {student['marks']:<5.1f}")
    print("=" * 60 + "\n")

    
    print(f"Step 4: Total student count in the database: {len(loaded_students)}")



if __name__ == "__main__":
    print("--- Student JSON Database System ---")
    student_json_database()
    
    