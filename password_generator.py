import random
import string


def password_generator(length, number_of_letters, number_of_numbers):
    if length < 6:
        print('Password should have a minimum of six(6) character: ')
        return

    if number_of_letters + number_of_numbers > length:
        print('sum of the number of letters and numers should be less than or requal to the length of the password')
        return

    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    password_characters = []

    for _ in range(number_of_letters):
        password_characters.append(random.choice(letters))

    for _ in range(number_of_numbers):
        password_characters.append(random.choice(numbers))

    remaining_content = length - number_of_letters - number_of_numbers
    for _ in range(remaining_content):
        password_characters.append(random.choice(numbers + letters + symbols))

    random.shuffle(password_characters)
    password = ''.join(password_characters)
    return password


if __name__ == "__main__":
    print("Password Generator")
    print("------------------")
    length = int(
        input("Enter the desired password length (minimum 6 characters): "))
    number_of_letters = int(
        input("Enter the number of letters you want in your password: "))
    number_of_numbers = int(
        input("Enter the number of numbers you want in your password: "))

    password = password_generator(length, number_of_letters, number_of_numbers)
    print("Generated Password:", password)
