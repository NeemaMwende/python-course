import re

def add_details(name, age, email, phone):
    return f"Name: {name}, Age: {age}, Email: {email}, Phone: {phone}"

def main():
    print("Welcome to Angel Hotel")
    
    # Get user input for name
    name = input("Please enter your name: ")

    # Get user input for age with validation
    while True:
        age = input("Please enter your age: ")
        if age.isdigit():
            age = int(age)
            break
        else:
            print("Invalid input. Please enter a valid age (integer).")
    
    # Get user input for email with validation
    email_pattern = r"[^@]+@[^@]+\.[^@]+"
    while True:
        email = input("Please enter your email (e.g., hushe@gmail.com): ")
        if re.match(email_pattern, email):
            break
        else:
            print("Invalid email format. Please enter a valid email (e.g., hushe@gmail.com).")
    
    # Get user input for phone number
    phone = input("Please enter your phone number: ")
    
    # Call the function to add the details
    result = add_details(name, age, email, phone)
    
    # Print the result
    print(f"Your details are: {result}")

# Execute the main function
if __name__ == "__main__":
    main()
