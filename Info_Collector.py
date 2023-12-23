# Import re library
import re
# Ask for the info from the user
def get_user_info():
    print("Welcome! Please provide the following information:")
    # Ask the user name
    while True:
        user_name = input("Name: ")
        if user_name.strip():
            break
    # If name is empty asks user to try again as it is a required field
        else:
            print("Name cannot be empty. Please try again.")
    
    while True:
        user_age = input("Age: ")
        if user_age.isdigit() and 0 <= int(user_age) <= 120:
            user_age = int(user_age)
            break
        else:
            print("Age must be a valid number between 0 and 120. Please try again.")
    
    while True:
        user_email = input("Email: ")
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(email_pattern, user_email):
            break
        else:
            print("Invalid email format. Please try again.")
    # Displays the details entered by the user
    return {
        "Name": user_name,
        "Age": user_age,
        "Email": user_email
    }

if __name__ == "__main__":
    user_info = get_user_info()
    
    print("\nThank you for providing your information!")
    print("Name:", user_info["Name"])
    print("Age:", user_info["Age"])
    print("Email:", user_info["Email"])
