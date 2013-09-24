"""
hangman.py
Adam Chin
22 Mar 2012
"""

import os

# clears terminal (on Unix and Windows)
def clear():
    os.system('cls' if os.name=='nt' else 'clear')


# draw hangman picture
def draw():
    state = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    print state[len(guessed)]


# get the letter guessed by the player and return it in lowercase
def get_letter():
    letter = raw_input('\nGuess a letter: ')
    while(len(letter) != 1 or not(letter.isalpha())):
        letter = raw_input('That\'s not a letter!\nTry again: ')
    return letter.lower()


# check if letter guessed is in the word; if so, 
# update progress list and return True, else return False
def check_guess(letter):
    index = 0
    flag = False
    for n in input:
        if letter == n:
            flag = True
            progress[index] = letter
        index += 1              
    return flag


# check to see if player has won
def check_win():
    return input == ''.join(progress)


"""main program logic"""

# get word from player, and ensure valid alphabetic input
input = raw_input('Enter the word to be guessed: ')
while not(input.isalpha()): 
    print 'Sorry, the string you have entered is invalid.'
    input = raw_input('Enter the word to be guessed: ')

clear()

progress = []   # letters guessed that are in input 
guessed = []    # letters guessed that are not in input
hanged = False

# prepare to display lines representing letters 
for letters in input:
    progress.append(' _ ')

# gameplay loop
draw()
while(not(check_win() )):
    print ''.join(progress)
    guess = get_letter()    
    
    # check for duplicate guesses
    if guess in guessed or guess in progress:
        clear()
        print 'You already guessed that, silly!' 
    else:    
        # if guess is in the word, congratulate player, otherwise
        # add guess to guessed list
        if check_guess(guess):
            clear()
            print 'Good guess!'
        else:
            guessed.append(guess) 
            clear()
            print 'Oh no!'
            if (len(guessed) == 6):
                hanged = True
                break

    # print a sorted list of letters already guessed for player's convenience 
    guessed.sort() 
    if len(guessed) > 0:
		print 'letters guessed: ',
		print ' '.join(guessed)
    draw()

# end gameplay loop


if hanged:
    print 'You were hanged =('
    draw()
    print 'The word was: ' + input
else:
    print 'You won! The word was: ' + input
