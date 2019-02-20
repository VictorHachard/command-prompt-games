from hangman import*
import random

wordToFind = ""
life = 0

def start():
    global wordToFind
    global life
    life = 0
    wordToFind = pickRandomWordInDictionary('words_english.txt')
    actualWord = "_" * len(wordToFind)
    while life <= 10:
        actualWord = askLetterAndHandle(actualWord)
        if actualWord == wordToFind:
            print("You Win\n")
            return
        elif life >= 10:
            print("You lose the word to find was: " + wordToFind + "\n")
            return

def askLetterAndHandle(actualWord):
    global life
    print("Actual word: " + str(actualWord))
    inputLetter = input("Enter a letter to test. \n")
    while len(inputLetter) != 1 or (inputLetter.isdigit()):
        inputLetter = input("That not a letter, enter a letter to test. \n")
    inputLetter.lower()
    if wordToFind.find(inputLetter) != -1 and actualWord.find(inputLetter) == -1:
        for indice in range(len(wordToFind)):
            new = list(actualWord)
            if wordToFind[indice] == inputLetter:
                new[indice] = inputLetter
            actualWord = ''.join(new)
    else:
        life += 1
        print(life)
    print("Actual word: " + actualWord)
    hangman(life)
    return actualWord

'''
Return a random word in the file given
arg file => the name of the file
return => the word
'''
def pickRandomWordInDictionary(file):
    with open(file) as files:
        maxNumber = sum(1 for _ in files)
    number = random.randint(0, maxNumber)
    file = open(file, "r")
    i = 0
    for line in file:
        if i == number:
            return line.strip()
        i += 1
    file.close()

'''
Return True if the word belong to the file given
arg file => the name of the file
arg word => the word to verify
return => a bollean
'''
def belongsToDictionary(word, file):
    with open(file) as file:
        for line in file:
            if line.strip() == word:
                return True
        return False

if __name__ == '__main__':

    while True:
        start()
