# Q5. File Reader System:
# Ask user for filename
# Open and read file
# Handle FileNotFoundError
# Check if file is empty
# Print total number of lines
# Add finally block

import os

def file_reader_system(filename: str) -> None:
   
    file_object = None
    print(f"\n--- Attempting to read file: '{filename}' ---")
    try:
       
        file_object = open(filename, 'r', encoding='utf-8')
        
      
        lines = file_object.readlines()
        
        
        if not lines:
            print(f"Status: The file '{filename}' exists but is EMPTY.")
            print("Total number of lines: 0")
        else:
            
            print("--- File Contents Start ---")
            for i, line in enumerate(lines, 1):
                print(f"Line {i}: {line.rstrip()}")
            print("--- File Contents End ---")
            
            
            print(f"Total number of lines: {len(lines)}")
            
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please check the file path.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
    finally:
        
        if file_object is not None:
            file_object.close()
            print(f"Resource Cleanup: File stream for '{filename}' has been closed.")
        else:
            print("Resource Cleanup: No file stream was opened to close.")
        print("File reading operation completed.")


if __name__ == "__main__":
    print("--- File Reader System ---")
    
    
    sample_file = "demo_test_file.txt"
    empty_file = "demo_empty_file.txt"
    
    print("\nCreating demo files for testing...")
    
    with open(sample_file, "w", encoding="utf-8") as f:
        f.write("Line 1: Hello World!\nLine 2: Welcome to Advanced Python.\nLine 3: File operations are fun.")
        
    
    with open(empty_file, "w", encoding="utf-8") as f:
        pass
        
    print(f"Demo files created: '{sample_file}' (with text), '{empty_file}' (empty).")


    try:
        user_input = input("\nEnter a filename to read (or press Enter to run automated tests): ").strip()
    except (EOFError, IOError):
        user_input = ""

    if user_input:
        file_reader_system(user_input)
    else:
        print("\n--- Running Automated Test Cases ---")
        
        
        file_reader_system(sample_file)
        

        file_reader_system(empty_file)
        
        
        file_reader_system("does_not_exist.txt")

    
    print("\nCleaning up demo files...")
    for file in [sample_file, empty_file]:
        if os.path.exists(file):
            try:
                os.remove(file)
                print(f"Removed temporary file: '{file}'")
            except Exception as e:
                print(f"Could not remove '{file}': {e}")
