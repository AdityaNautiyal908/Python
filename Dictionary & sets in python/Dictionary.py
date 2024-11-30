# Function to convert a string password to binary based on each digit's binary representation
def convert_to_binary(number):
    # If the number is a string of digits, convert each character to binary
    if isinstance(number, str):
        # Convert each digit to binary and return the combined result
        return ''.join(format(int(digit), '04b') for digit in number)
    # If the number is an integer, directly convert it to binary
    elif isinstance(number, int):
        return bin(number)[2:]  # bin() returns '0b' prefix, so we remove it
    else:
        raise ValueError("Input must be a number or a string of digits")

# Manually convert your password to binary
DB_PASSWORD_BINARY = "1000100101111001100000100110001100100001"

# Function to check if the entered password matches the binary password
def check_password():
    # Ask the user for the password (the password entered as digits)
    entered_password = input("Enter the password to run the code: ")

    # Convert entered password to binary
    entered_password_binary = convert_to_binary(entered_password)

    # Debug: print both the entered password's binary and the predefined binary
    print(f"Entered password binary: {entered_password_binary}")
    print(f"Expected binary password: {DB_PASSWORD_BINARY}")

    # Compare the entered binary password with the stored binary password
    if entered_password_binary != DB_PASSWORD_BINARY:
        print("Incorrect password. Access denied.")
        exit()  # Exit the program if the password is wrong

    print("Password accepted. You can now run the program.")

# Main program logic
def main_program():
    print("Running the main program...")

if __name__ == "__main__":
    check_password()
    main_program()




