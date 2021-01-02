import random


def generate_password():
    caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    symbols = ['!', '#', '$', '&', '/', '(', ')']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    characters = caps + lowercase + symbols + numbers

    password = []

    for i in range(20):
        caracter_random = random.choice(characters)
        password.append(caracter_random)

    password = "".join(password)
    return password


def run():
    password = generate_password()
    print('The new password is: ' + password)


if __name__ == '__main__':
    run()
