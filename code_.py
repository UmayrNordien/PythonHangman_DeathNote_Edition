import random
import time
import os

def play_again():
    question = 'Shall we play another round, human? (y/n)\n'
    play_game = input(question)
    
    # Validate user input
    while play_game.lower() not in ['y', 'n']:
        play_game = input(question)

    if play_game.lower() == 'y':
        return True
    else:
        return False

def hangman(word):
    display = '_' * len(word)
    count = 0
    limit = 6  # You have 6 lives, human.
    letters = list(word)
    guessed = []
    
    while count < limit:
        guess = input(f'Word of Fate: {display} Enter your guess, mortal:\n').strip()
        
        # Validate user input
        while len(guess) != 1 or not guess.isalpha():
            print('Invalid input. Enter a single letter, mortal.\n')
            guess = input(f'Word of Fate: {display} Enter your guess, mortal:\n').strip()

        if guess in guessed:
            print('Foolish human, you already attempted that guess. Try again.\n')
            continue

        if guess in letters:
            letters.remove(guess)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                display = display[:index] + guess + display[index + 1:]

        else:
            guessed.append(guess)
            count += 1
            print_hangman(count)
            print(f'Wrong guess, human. {limit - count} lives remaining.\n')

        if display == word:
            print(f'Congratulations, human. You have guessed the word "{word}" correctly.')
            break

    if count == limit:
        print('Oh well, your fate is sealed. You lose.')
        print(f'The true word was: "{word}".')

def print_hangman(count):
    hangman_stages = [
        '''
          ______
         |/     |
         |
         |
         |
         |
        _|_
        ''',
        '''
          ______
         |/     |
         |      O
         |
         |
         |
        _|_
        ''',
        '''
          ______
         |/     |
         |      O
         |      |
         |
         |
        _|_
        ''',
        '''
          ______
         |/     |
         |      O
         |     /|
         |
         |
        _|_
        ''',
        '''
          ______
         |/     |
         |      O
         |     /|\\
         |
         |
        _|_
        ''',
        '''
          ______
         |/     |
         |      O
         |     /|\\
         |     /
         |
        _|_
        ''',
        '''
          ______
         |/     |
         |      O
         |     /|\\
         |     / \\
         |
        _|_
        '''
    ]
    
    print(hangman_stages[count])

def play_hangman():
    print('Welcome to the Realm of Death, human.')
    name = input('What shall I call you? ')
    print(f'Greetings, {name}. Your fate awaits.')
    time.sleep(1)
    print('The game is about to begin...\nLet the guessing of fate commence.')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

    words_to_guess = [
        'shinigami', 'note', 'apples', 'justice', 'realm', 'destiny',
        'human', 'death', 'power', 'fate', 'light', 'ryuk', 'writing', 'l'
    ]
    play = True
    while play:
        word = random.choice(words_to_guess)
        hangman(word)
        play = play_again()

    print('Farewell, mortal. Until we meet again.')
    exit()

if __name__ == '__main__':
    play_hangman()