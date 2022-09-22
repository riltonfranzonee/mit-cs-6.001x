# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

from operator import le
import random
from tkinter import FALSE

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open('words.txt', 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return all(letter in lettersGuessed for letter in secretWord)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''

    for secretLetter in secretWord:
      if (secretLetter in lettersGuessed):
        result += secretLetter
      else:
        result += '_'

    return result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]

    available = list(set(alphabet) - set(lettersGuessed))

    available.sort()

    return ''.join(available)

def isValidLetter(input):
  alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]

  return input in alphabet


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print('-----------')

    lettersGuessed = []
    maxAttempts = 8
    failedAttempts = 0
    guessed = False

    availableAttempts = maxAttempts - failedAttempts

    while(availableAttempts > 0):
      availableLetters = getAvailableLetters(lettersGuessed)

      print("You have " + str(availableAttempts) + " guesses left.")
      print("Available letters: " + availableLetters)
      guess = input("Please guess a letter: ").lower()

      feedbackMessage = ''
      if(len(guess) > 1):
        print('Invalid input! You should only add one character at a time')
        print('-----------')
        continue
      elif (guess in lettersGuessed):
        feedbackMessage = "Oops! You've already guessed that letter: "
      elif(not guess in availableLetters):
        print('Invalid input! You should enter a valid letter')
        print('-----------')
        continue
      elif(guess in secretWord):
        lettersGuessed.append(guess)
        feedbackMessage = 'Good guess: '
      else:
        feedbackMessage = 'Oops! That letter is not in my word: '
        failedAttempts += 1
        availableAttempts = maxAttempts - failedAttempts
        lettersGuessed.append(guess)

      feedbackMessage += getGuessedWord(secretWord, lettersGuessed)

      print(feedbackMessage)
      print('-----------')

      guessed = isWordGuessed(secretWord, lettersGuessed)

      if(guessed):
        break

    if(guessed):
      print('Congratulations, you won!')
    else:
      print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')


hangman('rilton')
      





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
