# Q10. API Task:
# Use requests
# API: https://jsonplaceholder.typicode.com/users
# Check status code == 200
# Print Name, Email, Phone of all users
# Save data to users.json
# Print total users fetched
# Handle all exceptions properly

import json
import sys

try :
    
    import requests
except ImportError:
    print("Error: The 'requests' library is not installed.")
    print("Please install it using: pip install requests")
    sys.exit(1)

def fetch_and_save_users() -> None:
    
    api_url = "https://jsonplaceholder.typicode.com/users"
    output_filename = "users.json"
    
    print(f"Connecting to API: {api_url} ...")
    try:
        
        response = requests.get(api_url, timeout=10)
        
        
        if response.status_code == 200:
            print("Successfully fetched data! Status Code: 200 OK\n")
            
            
            try:
                users_data = response.json()
            except ValueError as json_err:
                print(f"Failed to parse JSON response: {json_err}")
                return
            
            
            print("=" * 80)
            print(f"{'Name':<25} | {'Email':<30} | {'Phone':<20}")
            print("-" * 80)
            for user in users_data:
                name = user.get("name", "N/A")
                email = user.get("email", "N/A")
                phone = user.get("phone", "N/A")
                print(f"{name:<25} | {email:<30} | {phone:<20}")
            print("=" * 80 + "\n")
            
            
            print(f"Saving data to '{output_filename}'...")
            try:
                with open(output_filename, "w", encoding="utf-8") as file:
                    json.dump(users_data, file, indent=4)
                print(f"Data saved successfully to {output_filename}.\n")
            except Exception as file_err:
                print(f"Error saving to JSON file: {file_err}")
            
            
            total_users = len(users_data)
            print(f"Total users fetched and saved: {total_users}")
            
        else:
            print(f"Failed to fetch data. Server returned Status Code: {response.status_code}")
            
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please check your internet connection and try again.")
    except requests.exceptions.ConnectionError:
        print("Error: A Connection error occurred. Check your internet connection or the server URL.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred while handling the network request: {req_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    print("--- API Users Fetching Task ---")
    fetch_and_save_users()
