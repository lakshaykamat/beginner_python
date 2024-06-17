from generate_password import generate_password


def get_yes_or_no_response(message):
    response = None
    while response is None:
        response = input(message)
        if response.lower() not in ['y', 'n']:
            print("Invalid input. Please enter 'y' or 'n'.")
            response = None
    return response.lower() == 'y'


while True:
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Password length should be greater than 0.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

have_digits = get_yes_or_no_response("Do you want numbers in the password? (y/n): ")
have_pun = get_yes_or_no_response("Do you want special characters in the password? (y/n): ")
password = generate_password(length, have_digits, have_pun)
print("Generated Password:", password)
