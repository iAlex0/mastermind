import random
import os

COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code  = []
    for _ in range(CODE_LENGTH):
        code.append(random.choice(COLORS))

    return code

def guess_code():
    while True:
        guess = input("\033[32mGuess:\033[0m ").upper().strip().split(' ')
        
        if len(guess) != CODE_LENGTH:
            print(f"Please enter {CODE_LENGTH} colors")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Please enter valid colors: {COLORS}")
                break
        else:
            break

    return guess    


def check_code(guess, real_code):
    color_count = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_count:
            color_count[color] = 0
        color_count[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_count[real_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color != real_color and guess_color in color_count and color_count[guess_color] > 0:
            incorrect_pos += 1
            color_count[guess_color] -= 1

    return correct_pos, incorrect_pos



def game():
    print(f'Welcome to mastermind, you have {TRIES} tries to guess the code...')
    print('-' * 20)
        
    real_code = generate_code()
    for attempts in range(1, TRIES + 1):
        print(f'Valid colors: ', COLORS)
        print('\033[34m' + 'Example: R G B Y' + '\033[0m\n')
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, real_code)

        if correct_pos == CODE_LENGTH:
            print('\n\033[34m' + f'You won in {attempts} attempts!' + '\033[0m')
            break

        print('\033[33m' + f'Correct position: {correct_pos} | Incorrect position: {incorrect_pos}' + '\033[0m')
        print('-' * 20)
    else:
       print('\033[31m' + f'You lost, the code was: {real_code}' + '\033[0m')

if __name__ == '__main__':
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # clear console
        game()
        again = input('Play again? (y/n): ')
        if again.lower() == 'n':
            break


