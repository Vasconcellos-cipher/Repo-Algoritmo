import random

def game_guessing(chances):
    print(f"You have {chances} chances to guess the correct number.")
    secret_number = random.randint(1, 100)
    attempts = 0

    while attempts < chances:
        try:
            answer = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if answer < 1 or answer > 100:
            print("Please enter a number between 1 and 100!")
            continue

        attempts += 1

        if answer == secret_number:
            print(f"Congratulations, you got it right in {attempts} attempts.")
            break

        elif answer < secret_number:
            print(f"The secret number is greater than {answer}.")
            print(f"You have {chances - attempts} attempt(s) left.")

        else:
            print(f"The secret number is smaller than {answer}.")
            print(f"You have {chances - attempts} attempt(s) left.")
    else:
        print(f"Game over! The number was {secret_number}.")

while True:
    print('''
        Welcome to the Number Guessing Game!
        I'm thinking of a number between 1 and 100.
    ''')

    try:
        select = int(input('''Please select the difficulty level:
            1. Easy (10 chances)
            2. Medium (5 chances)
            3. Hard (3 chances)
            4. Exit!
            Enter your choice:  '''))
    except ValueError:
        print("invalid input")

    else:
        if select == 1:
            print('''\nGreat! You have selected the Easy difficulty level.
            Let's start the game!\n''')
            game_guessing(10)

        elif select == 2:
            print('''\nGreat! You have selected the Medium difficulty level.
            Let's start the game!\n''')
            game_guessing(5)

        elif select == 3:
            print('''\nGreat! You have selected the Hard difficulty level.
            Let's start the game!\n''')
            game_guessing(3)

        elif select == 4:
            print("\nCome back again!")
            break
        else:
            print("invalid option!")

    
