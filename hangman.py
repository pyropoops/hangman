from os import path
import random
import time
import json

def loadData(filepath):
    try:
        if path.exists(filepath):
            with open(filepath, "r") as file:
                return json.load(file)
    except:
        pass
    
    return {"wordlist": []}


class Hangman:
    def __init__(self, dataFileLoc):
        self.dataFileLoc = dataFileLoc
        self.wordList = loadData(dataFileLoc)["wordlist"]


    def start(self):
        word = random.choice(self.wordList)
        solvedLetters = [" "]
        triedLetters = []
        isWordSolved = False
        
        while not isWordSolved:
            solved = True
            
            obfuscatedText = ""

            for c in word:
                if not c in solvedLetters:
                    obfuscatedText += "_"
                    solved = False
                else:
                    obfuscatedText += c

            if solved: 
                isWordSolved = True

            print(obfuscatedText, "\n")

            letter = input("Please try a letter\n")

            if len(letter) != 1:
                print("You can only pick one letter at a time!")
                return

            if letter == " ":
                print("Excuse me, you're not funny with that space business!")
                return

            if letter in triedLetters:
                print("You already tried that!")
                return

            triedLetters.append(letter)

            if letter in word:
                print("That letter was in the word!!")
                solvedLetters.append(letter)

            

hangman = Hangman("data.json")
hangman.start()