menu_options = ["Encode", "Decode", "Quit"]


# Define the encoder function
def encode_password(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password


# Define the decoder function
def decode_password(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password


# Define the main function
def main():
    while True:
        # Print the menu options
        print("Menu")
        print("-------------")
        for i, option in enumerate(menu_options):
            print(f"{i + 1}. {option}")

        # Get the user's option
        option = input("\nPlease enter an option: ")

        # Perform the selected action
        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode_password(password)
            print("Your password has been encoded and stored!")
        elif option == "2":
            encoded_password = input("Please enter your password to decode: ")
            decoded_password = decode_password(encoded_password)
            print(f"Your decoded password is: {decoded_password}")
        elif option == "3":
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
