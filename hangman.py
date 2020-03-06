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
    
    return {"wordlist": ["croug is smart", "croug is dumb", "iphone", "mum", "ladder", "handbag"]}


class Hangman:
    def __init__(self, dataFileLoc):
        self.dataFileLoc = dataFileLoc
        self.wordList = loadData(dataFileLoc)["wordlist"]
        self.lives = 8

    def start(self):
        word = random.choice(self.wordList)
        solvedLetters = [" "]
        triedLetters = []
        isWordSolved = False
        
        while not isWordSolved and self.lives > 0:
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
                break

            print(obfuscatedText, "\n")

            print("You have", str(self.lives), "lives!")
            letter = input("Please try a letter\n")

            if len(letter) != 1:
                print("You can only pick one letter at a time!")
                break

            elif letter == " ":
                print("Excuse me, you're not funny with that space business!")

            elif letter in triedLetters:
                print("You already tried that!")

            triedLetters.append(letter)

            if letter in word:
                print("That letter was in the word!!")
                solvedLetters.append(letter)

            else:
                print("That letter was not in the word! That's very unfortunate for you! Loser. You lost a life!")
                self.lives -= 1
        if isWordSolved:
            print("Congratulations! You won the game and you actually didn't die! Wow!")
        else:
            print("You lost, you absolute disgrace.")
        if input("Play again (y/n)? ").lower() == "y":
            self.start()

hangman = Hangman("data.json")
hangman.start()
