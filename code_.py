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

# Define hints for each word
hints = {
    "shinigami": "A Japanese spirit of death.",
    "note": "The means of death.",
    "apples": "A favorite snack of Shinigami.",
    "justice": "Light and L have their own views on the pursuit of justice.",
    "realm": "The supernatural realm where Shinigami reside.",
    "destiny": "The concept of fate.",
    "human": "The main characters are all humans with different motivations.",
    "death": "A central theme in 'Death Note,' as the characters deal with the power to kill.",
    "power": "The Death Note grants its user immense power over life and death.",
    "fate": "The idea of fate and predetermined outcomes is a recurring motif.",
    "light": "The first name of the main character, Light Yagami, who becomes Kira.",
    "ryuk": "A Shinigami who drops the Death Note into the human world.",
    "writing": "Characters carry out their actions by writing names in the Death Note.",
    "L": "The initial pseudonym of the genius detective, whose true name is a mystery.",
    "investigation": "The series revolves around an intense cat-and-mouse investigation.",
    "notebook": "Another name for the Death Note, a key element of the story.",
    "kira": "The alias used by Light Yagami as he takes on the role of a vigilante killer.",
    "consequences": "The series explores the moral and ethical consequences of using the Death Note.",
    "suspense": "The story is filled with suspense as characters try to outsmart each other.",
    "mind": "A central element of the story, as characters use their intelligence to outwit their opponents.",
    "rule": "The Death Note comes with a set of rules that must be followed.",
    "criminal": "Light Yagami begins his journey as Kira by targeting criminals.",
    "intelligence": "Both Light and L are highly intelligent characters.",
    "plot": "The intricate plot of 'Death Note' keeps viewers and readers engaged.",
    "puzzle": "Solving the puzzle of Kira's identity is a key aspect of the story.",
    "penalty": "The Death Note has severe penalties for misuse.",
    "game": "'Death Note' is a psychological game between Light and L.",
    "mystery": "The series is filled with mysteries, from character motivations to plot twists.",
    "prosecutor": "Characters like L and Near take on the role of prosecutors in pursuit of Kira.",
    "law": "The legal system and its manipulation are central to the story.",
    "control": "Light seeks control over the world using the Death Note.",
    "secret": "The Death Note and its users keep their actions a secret.",
    "detective": "L and other characters work as detectives to solve the Kira case.",
    "strategy": "Characters employ various strategies to achieve their goals.",
    "enigma": "The true identity of L and Kira is an enigma.",
    "chess": "The cat-and-mouse game between Light and L resembles a game of chess.",
    "lawyer": "Characters like Teru Mikami have legal backgrounds.",
    "code": "The Death Note has a code of rules.",
        "judgment": "Characters take on the role of judge and executioner.",
    "elimination": "Kira seeks the elimination of criminals.",
    "cat and mouse": "The central theme of the series is the cat-and-mouse chase between Light and L.",
    "clue": "Clues and hints are scattered throughout the story.",
    "misa": "A key character in the series, obsessed with Kira.",
    "near": "A successor to L in the pursuit of Kira.",
    "mello": "Another successor to L with a different approach.",
    "soichiro": "Light's father and a police officer.",
    "sayu": "Light's younger sister.",
    "rem": "A Shinigami with a significant role in the story.",
    "teru": "Teru Mikami, a devoted follower of Kira.",
    "matsuda": "A member of the police task force.",
    "aizawa": "Another member of the police task force.",
    "ide": "A detective working on the Kira case.",
    "mikami": "Teru Mikami, a prosecutor and Kira supporter.",
    "mogi": "Another member of the police task force.",
    "ukita": "A detective in the series.",
    "naomi": "Naomi Misora, a former FBI agent in pursuit of Kira.",
    "raye": "Raye Penber, an FBI agent involved in the case.",
    "halle": "Halle Lidner, a member of the SPK organization.",
    "watari": "The caretaker of L and a key figure in the story."
}

def hangman(word):
    display = '_' * len(word)
    count = 0
    limit = 6  # You have 6 lives, human.
    letters = list(word)
    guessed = []
    
    hints_used = 0
    max_hints = 3  # Hints allowed.

    while count < limit:
        guess = input(f'Word of Fate: {display} Enter your guess, mortal:\n').strip()
        
        if guess.lower() == "hint":
            if hints_used < max_hints:
                word_hint = hints.get(word, "No hint available.")
                print(f"Hint: {word_hint}")
                hints_used += 1
            else:
                print("You've used all your hints...too bad.")
            continue

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
        print(f'You lost, human. The word was "{word}".')
        
        # Ryuk ascii art
        print("""
                ⠀⠀⠀⠀⠀⠀⠀⢀⣰⣸⣤⣆⡀⠀⠀⠀⠀⠀⠀⠀
                ⠉⠀⠢⣭⣼⣶⣄⣼⣿⣿⣿⣿⡧⣀⣠⣀⣤⡀⠀⠀
                ⠂⡩⢔⣿⣿⣿⡿⢿⣁⠙⢉⣿⣿⢿⣿⣿⣷⡦⢤⡀
                ⠀⡰⡹⣿⣿⣿⣧⠘⢮⣉⣹⠋⠁⣾⣿⣿⣿⠦⡁⠊
                ⠊⠐⢰⣾⡿⡏⠻⣷⣾⣭⣿⣴⣾⣿⣿⣿⣿⡕⠛⠄
                ⠀⢀⣼⡿⠁⠀⠀⠀⢻⣿⣿⣿⡿⠁⠀⠀⠹⣿⣄⠀
                ⠀⣼⣿⠁⠀⠀⠀⣤⣾⣿⣿⣿⣷⣄⠀⠀⠀⠻⣿⣆
                ⠈⠿⣿⡄⠀⠀⣠⣭⣿⣿⣻⣿⣿⣿⡄⠀⠀⠀⣿⡟
                ⠀⠀⣿⡇⢀⣾⣟⣿⣿⣿⣿⣿⣿⣿⣿⣀⠀⠀⣿⠃
                ⠀⠀⢸⣧⠀⣿⣿⠟⡿⡿⢻⠿⣿⣿⣿⣿⡄⠀⣿⠀
                ⠀⠀⢤⣿⣼⣿⠏⠀⠃⠁⠈⠀⠁⢻⣯⣏⠀⢸⣿⠀
                ⠀⠀⢀⢋⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣤⣿⣿⠀
                ⠀⠀⣾⣺⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⢰⣿⡏⢸⡿⡇
                ⠀⠀⠈⠻⡾⢿⣧⠀⠀⠀⠀⠀⠀⠀⢸⣿⠁⣾⡾⠁
                ⠀⠀⠀⠀⠀⠘⣿⡀⠀⠀⠀⠀⠀⠀⢸⡟⠀⠈⠀⠀
                ⠀⠀⠀⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⢀⣿⠃⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀
        """)
        print(f'The true word was: "{word}".')

def print_hangman(count):
    hangman_stages = [
        '''
         ╭──────╮
         ┊/     ┊
         ┊
         ┊
         ┊
         ┊
        _┊_
        ''',
        '''
         ╭──────╮
         ┊/     ┊
         ┊      O
         ┊
         ┊
         ┊
        _┊_
        ''',
        '''
         ╭──────╮
         ┊/     ┊
         ┊      O
         ┊      ┊ 
         ┊
         ┊
        _┊_
        ''',
        '''
         ╭──────╮
         ┊/     ┊
         ┊      O
         ┊     /┊ 
         ┊
         ┊
        _┊_
        ''',
        '''
         ╭──────╮
         ┊/     ┊ 
         ┊      O
         ┊     /┊\\
         ┊
         ┊
        _┊_
        ''',
        '''
         ╭──────╮
         ┊/     ┊ 
         ┊      0
         ┊     /┊\\
         ┊     /
         ┊
        _┊_
        ''',
        '''
         ╭──────╮
         ┊/     ┊ 
         ┊      0
         ┊     /┊\\
         ┊     / \\
         ┊
        _┊_         ✝ RIP ꧂ 
        '''
    ]
    
    print(hangman_stages[count])

def play_hangman():
    print('Welcome to the Realm of Death, human.')
    print("""
        ⠀⠀⠀⠀⠀⠰⣄⠀⠀⠀⠈⢻⣇⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢰⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠
        ⠀⠀⠀⠀⠀⠀⠈⠳⢦⡀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣏⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢶⡀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⢿⣿⣷⣶⣦⣀⣀⣠⣶⣿⣿⣿⣿⣿
        ⠀⠀⠀⠀⠀⢀⡀⠀⠀⠈⣄⡰⠁⠀⠀⠀⠲⣤⡀⠀⠀⠀⠀⣠⠚⠁⠀⠀⠀⠀⠀⢀⣀⠀⣼⠃⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⠀⠀⠀⠀⠀⠀⠙⢀⣴⡞⠋⢸⣦⣶⣶⣤⣄⠈⢳⡀⠀⢀⡞⠁⠀⣠⣴⣶⣾⣿⣿⣿⣵⣾⡟⠀⠀⢸⡿⣿⣿⣿⠋⣁⢄⡙⣿⣿⣿⣿
        ⠀⠀⠀⠀⠀⠀⢀⠘⠻⣄⠀⢈⣿⡟⣯⡍⠻⣷⡀⠃⠀⢿⠄⢀⣾⣿⠋⣭⣭⠙⢿⣿⣿⡿⠁⠀⢀⡞⠀⣿⡟⢻⠏⠁⢠⡇⣽⣿⣿⣿
        ⠀⠀⠲⢄⠀⠀⠀⠀⠀⠙⢷⣸⢹⡟⢿⡿⠀⢹⣷⡀⠀⠀⢰⡿⣿⡇⠀⢿⡿⠃⢈⣿⡟⠀⠀⠀⣼⡇⠀⣿⠃⠈⡇⠈⡟⢰⣿⣿⣿⣿
        ⠀⠀⠀⠀⠙⠲⢤⣀⠀⠀⠀⢻⢸⣿⣦⣤⣴⡿⢿⠗⠀⠀⠈⠁⢻⣿⣦⣤⣤⣤⣾⠿⠋⠁⠀⣰⣿⠁⠀⠿⢠⣞⣠⡾⠃⣼⣿⡿⠛⣿
        ⠷⣶⣤⣀⠀⠀⠀⠈⠙⠲⢤⣘⡆⠀⠉⠉⠀⡰⣿⠆⠀⣌⠱⣤⡀⠀⠀⠀⢄⠀⠀⠀⠀⣤⣾⣿⣿⠀⠀⠀⢈⣿⣩⣴⣿⣿⠟⠀⠀⠀
        ⡀⠀⠈⠙⠛⠶⡄⠀⠀⠀⠀⠀⢹⣤⡇⠀⠀⠠⣧⠀⠀⠘⡄⠈⢻⡇⠀⠀⠈⣟⢦⣀⣼⣿⣿⠏⠀⠀⠀⣰⣿⣿⠁⠀⠙⠁⠀⠀⠀⠀
        ⣿⣷⣶⢤⣤⣀⠀⠀⠀⠀⠀⠀⣼⢿⡇⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⢸⣶⣿⣿⣿⡟⠀⠀⠀⢰⠇⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣌⣳⡦⢤⣤⣤⣤⣤⣤⣤⣤⣤⣶⣶⣶⣶⣿⣾⣿⣿⣿⣧⣶⠀⠀⡞⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
        ⣤⣤⣤⣤⣀⣀⣀⡀⠀⠀⠀⠀⠀⠈⢻⡿⢿⣿⢿⣿⣿⣿⣿⣿⣿⣿⡿⣿⠿⣿⡾⢻⣿⣿⠟⡟⠀⢸⠇⢰⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
        ⠟⠛⠛⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⢠⣿⣾⡿⣷⣻⡿⣷⢻⣿⣿⣾⣿⣿⣾⢏⣴⡿⠟⠁⢰⠃⠀⣼⠀⣀⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀
        ⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣀⠀⠀⠀⢿⡉⠛⠛⠛⣉⣛⣻⣿⣟⠾⠷⠿⢛⣡⣿⠏⠀⠀⠀⡼⠀⣠⠏⢸⠐⡌⡏⣹⡇⠀⠀⠀⠀⠀⠀
        ⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠖⣻⡟⠛⠛⠉⠉⠉⠙⠛⠛⠻⠿⠿⠛⠁⠀⢀⣠⢞⣡⠞⠁⠀⠀⠑⢿⡿⠋⠀⠀⠀⠀⠀⠀⠀
        ⣶⣶⣶⣶⣶⠶⠶⠶⠒⠂⠀⠀⠀⠘⣛⣏⢧⢀⣠⠆⠀⠀⠀⠘⢦⡀⠀⠀⣀⡤⠖⢋⡀⠊⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
        ⠛⢋⣉⣠⣤⣤⠤⠀⠀⠀⠀⢀⡴⢋⣡⡽⠛⢻⡏⠀⠀⠀⠀⠀⠈⢿⣛⣛⠋⠀⡠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠘⠇⠀⠀⠀⠀⠀⠀⠀⠀
        ⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⣯⣴⣿⠋⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠉⡸⠁⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)
    time.sleep(2)   # time.sleep function adds delay to a execution
    name = input('What shall I call you? ')
    time.sleep(2)
    print(f'Greetings, {name}. Your fate awaits.')
    time.sleep(2)  
    print('The game is about to begin...')
    time.sleep(2)  
    print('Let the guessing of fate commence.')
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

    words_to_guess = [
    'shinigami', 'note', 'apples', 'justice', 'realm', 'destiny',
    'human', 'death', 'power', 'fate', 'light', 'ryuk', 'writing', 'L',
    'investigation', 'notebook', 'Kira', 'consequences', 'suspense', 'mind', 'rule',
    'criminal', 'intelligence', 'plot', 'puzzle', 'penalty', 'game', 'mystery',
    'prosecutor', 'law', 'control', 'secret', 'detective', 'strategy', 'enigma',
    'chess', 'lawyer', 'code', 'judgment', 'elimination', 'cat and mouse', 'clue',
    'misa', 'near', 'mello', 'soichiro', 'sayu', 'rem', 'teru', 'matsuda',
    'aizawa', 'ide', 'mikami', 'mogi', 'ukita', 'naomi', 'raye', 'halle', 'watari'
    ]
    play = True
    while play:
        word = random.choice(words_to_guess)
        hangman(word)
        play = play_again()

    print('Farewell, mortal. Until we meet again.')
    print('*＊✿❀❀✿＊*')
    time.sleep(2)

    print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
    print('visit the developer\'s socials: https://linktr.ee/umayrnordien')
    print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')

if __name__ == '__main__':
    play_hangman()
