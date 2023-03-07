# Malika Saidmuradova 03/07/2023 
menu_options = ["Encode", "Decode", "Quit"]


# Define the encoder function
def encode_password(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password


# Define the decoder function



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
            # Partner decodes password
            
        elif option == "3":
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
