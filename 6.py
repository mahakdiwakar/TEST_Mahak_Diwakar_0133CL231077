# Q6. List & Tuple Operations:
# Create list of 8 city names
# Print first 4 cities
# Print last 4 cities
# Add a city
# Remove first city
# Convert list to tuple and print

def list_and_tuple_operations() -> None:
    
    
    cities = ["Mumbai", "New York", "London", "Tokyo", "Paris", "Sydney", "Berlin", "Dubai"]
    print("Initial list of cities:")
    print(cities)
    print(f"Total cities: {len(cities)}\n")

    
    first_four = cities[:4]
    print("First 4 cities:")
    print(first_four)
    print()


    last_four = cities[-4:]
    print("Last 4 cities:")
    print(last_four)
    print()

    
    new_city = "Singapore"
    cities.append(new_city)
    print(f"Added city '{new_city}':")
    print(cities)
    print()

    
    removed_city = cities.pop(0)
    print(f"Removed first city '{removed_city}':")
    print(cities)
    print()

    
    cities_tuple = tuple(cities)
    print("Converted list to a tuple:")
    print(cities_tuple)
    print(f"Data type: {type(cities_tuple)}")



if __name__ == "__main__":
    print("--- List and Tuple Operations Demo ---")
    list_and_tuple_operations()
