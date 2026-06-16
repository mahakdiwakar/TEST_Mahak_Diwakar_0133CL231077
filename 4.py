# Q4. Student Registration System:
# Custom Exception: InvalidAgeError
# Custom Exception: InvalidMarksError
# Input: name, age, marks
# Age must be between 15 and 30
# Marks must be between 0 and 100
# Handle exceptions properly
# Add a finally block

class InvalidAgeError(Exception):
    
    def __init__(self, age, message="Age must be between 15 and 30"):
        self.age = age
        self.message = f"{message} (Provided: {age})"
        super().__init__(self.message)


class InvalidMarksError(Exception):
   
    def __init__(self, marks, message="Marks must be between 0 and 100"):
        self.marks = marks
        self.message = f"{message} (Provided: {marks})"
        super().__init__(self.message)


def register_student(name: str, age_str: str, marks_str: str) -> None:
    
    print(f"\n--- Initiating Registration for: '{name}' ---")
    try:
        
        if not name.strip():
            raise ValueError("Student name cannot be empty.")

        
        try:
            age = int(age_str)
        except ValueError:
            raise ValueError(f"Age must be a valid integer. Got: '{age_str}'")

        if not (15 <= age <= 30):
            raise InvalidAgeError(age)

        
        try:
            marks = float(marks_str)
        except ValueError:
            raise ValueError(f"Marks must be a valid number. Got: '{marks_str}'")

        if not (0 <= marks <= 100):
            raise InvalidMarksError(marks)

        
        print(f"Registration Successful! Welcome {name} (Age: {age}, Marks: {marks})")

    except ValueError as e:
        print(f"Value Error during registration: {e}")
    except InvalidAgeError as e:
        print(f"Age Validation Failed: {e}")
    except InvalidMarksError as e:
        print(f"Marks Validation Failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        
        print(f"Registration attempt for '{name}' completed.")



if __name__ == "__main__":
    print("--- Student Registration System ---")
    
    
    try:
        user_choice = input("Do you want to enter details manually? (yes/no): ").strip().lower()
    except (EOFError, IOError):
        
        user_choice = "no"

    if user_choice in ("yes", "y"):
        try:
            name_input = input("Enter Student Name: ")
            age_input = input("Enter Student Age (15-30): ")
            marks_input = input("Enter Student Marks (0-100): ")
            register_student(name_input, age_input, marks_input)
        except Exception as e:
            print(f"Error reading inputs: {e}")
    else:
        print("\n--- Running Simulated Automated Test Cases ---")
        
        
        register_student("Alice", "20", "85.5")
        
        
        register_student("Bob", "12", "90")
        
        
        register_student("Charlie", "35", "75")
        
        
        register_student("Diana", "18", "120")
        
        
        register_student("Ethan", "22", "-5")
        
        
        register_student("Fiona", "twenty", "ninety")
