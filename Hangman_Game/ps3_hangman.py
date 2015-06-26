#  As a part of python learning course
# 
# Hangman game = Interactive word game"
#

# -----------------------------------
# 
# A simple word guessing game
# Author : Nachiappan Chockalingam
# Version 1.0.1 

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
secretWord = chooseWord(wordlist).lower()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    ret_bool = True
    for ch in secretWord:
        if ch not in lettersGuessed :
            ret_bool = False
            return ret_bool
    return ret_bool



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guess_word = ''
    for ch in secretWord:
        if ch in lettersGuessed:
            guess_word += ch
        else:
            guess_word += '_'
    return guess_word



def getAvailableLetters(lettersGuessed):
    
    avail_letters = 'abcdefghijklmnopqrstuvwxyz'
    for letter in lettersGuessed:
        avail_letters = avail_letters.replace(letter,'')
    return avail_letters
    

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
    word_len = len(secretWord)
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " +str(word_len)+" letters long."
    print "-------------"
    game_end = False
    lettersGuessed = list()
    Num_guess_left = 8
    guess_letter = ''
    guessed_word = ''
    while not game_end:
        print "You have "+str(Num_guess_left)+" guesses left."
        print "Available letters: " + getAvailableLetters(lettersGuessed)
        guess_letter = raw_input("Please guess a letter: ")
        guess_letter = guess_letter.lower()
        # if the letter has already been guessed
        if guess_letter in lettersGuessed:
            print "Oops! You've already guessed that letter: " + guessed_word
            print "------------"
            continue
        
        lettersGuessed.append(guess_letter)
        guessed_word = getGuessedWord(secretWord, lettersGuessed)
        
        #Validate the Guess
        if guess_letter in secretWord:
            print "Good guess: " + guessed_word
        else:
            print "Oops! That letter is not in my word: " + guessed_word
            Num_guess_left -= 1
            
        print "------------" 
        
        # Check for word guessed
        if isWordGuessed(secretWord, lettersGuessed):
            print "Congratulations, you won!"
            game_end = True
            break
        if Num_guess_left == 0:
            print "Sorry, you ran out of guesses. The word was %s." %secretWord
            break
            
        game_end = isWordGuessed(secretWord, lettersGuessed) or (Num_guess_left == 0 )
hangman(secretWord)






