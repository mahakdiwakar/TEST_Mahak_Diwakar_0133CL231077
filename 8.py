# Q8. Employee File Handling System:
# Create employees.txt
# Write 5 employees with salary
# Read and display contents
# Append 2 more employees
# Read updated contents
# Check existence using os.path.exists()
# Delete file

import os

def employee_file_handling_system() -> None:
    """
    Performs file Operations on employees.txt including creation, writing, reading,
    appending, existence checking, and deleting.
    """
    filename = "employees.txt"
    
    # 1. Create employees.txt and write 5 employees with salary
    print("Step 1: Creating 'employees.txt' and writing 5 initial employee records...")
    initial_employees = [
        "E101, Alice Smith, 75000\n",
        "E102, Bob Johnson, 62000\n",
        "E103, Charlie Brown, 54000\n",
        "E104, Diana Prince, 95000\n",
        "E105, Evan Wright, 48000\n"
    ]
    
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(initial_employees)
    print("Initial records written successfully.\n")

    # 2. Read and display contents
    print("Step 2: Reading and displaying 'employees.txt' contents:")
    print("=" * 45)
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read().rstrip())
    print("=" * 45 + "\n")

    # 3. Append 2 more employees
    print("Step 3: Appending 2 more employee records...")
    additional_employees = [
        "E106, Fiona Gallagher, 68000\n",
        "E107, George Costanza, 51000\n"
    ]
    with open(filename, "a", encoding="utf-8") as file:
        file.writelines(additional_employees)
    print("Additional records appended successfully.\n")

    # 4. Read updated contents
    print("Step 4: Reading and displaying updated 'employees.txt' contents:")
    print("=" * 45)
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read().rstrip())
    print("=" * 45 + "\n")

    # 5. Check existence using os.path.exists()
    print("Step 5: Checking file existence using os.path.exists()...")
    if os.path.exists(filename):
        print(f"File '{filename}' exists: YES")
    else:
        print(f"File '{filename}' exists: NO")
    print()

    # 6. Delete file
    print(f"Step 6: Deleting file '{filename}'...")
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting file: {e}")
    print()

    # Verify deletion
    print("Step 7: Verifying file deletion with os.path.exists()...")
    if os.path.exists(filename):
        print(f"File '{filename}' still exists: YES")
    else:
        print(f"File '{filename}' still exists: NO (Successfully Deleted)")


# Example execution and testing code
if __name__ == "__main__":
    print("--- Employee File Handling System Demo ---")
    employee_file_handling_system()
