# Q2. Create inheritance program:
# Person -> walk(), talk()
# Teacher(Person) -> teach()
# Student(Person) -> study()
# Create objects and call all methods including inherited methods.

class Person:
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def walk(self) -> None:
        
        print(f"{self.name} is walking.")

    def talk(self) -> None:
        
        print(f"{self.name} says: 'Hello! Nice to meet you.'")


class Teacher(Person):
    
    def __init__(self, name: str, age: int, subject: str):
        super().__init__(name, age)
        self.subject = subject

    def teach(self) -> None:
        
        print(f"Teacher {self.name} is teaching {self.subject}.")


class Student(Person):
    
    def __init__(self, name: str, age: int, grade: str):
        super().__init__(name, age)
        self.grade = grade

    def study(self) -> None:
        
        print(f"Student {self.name} is studying for grade {self.grade}.")


# Example execution and testing code
if __name__ == "__main__":
    print("--- Testing Inheritance Program ---")

    # Create a Teacher object
    print("\nInitializing Teacher object:")
    teacher = Teacher(name="Mr. Smith", age=45, subject="Physics")
    
    # Call inherited and specific methods for Teacher
    teacher.walk()       # Inherited from Person
    teacher.talk()       # Inherited from Person
    teacher.teach()      # Specific to Teacher

    # Create a Student object
    print("\nInitializing Student object:")
    student = Student(name="John Doe", age=16, grade="10th")
    
    # Call inherited and specific methods for Student
    student.walk()       # Inherited from Person
    student.talk()       # Inherited from Person
    student.study()      # Specific to Student
