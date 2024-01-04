import time
import random
import os
from urllib.request import urlopen
print("Hello Game master, this is Dylans hangman simulator rtx 2000")
#finds random word
word = ""
while len(word) < 3 or len(word) > 7:
    #rolls random word
    txt = urlopen("https://www.mit.edu/~ecprice/wordlist.10000").read()
    WORDS = txt.splitlines()
    word = str(random.choice(WORDS))

    #cleans word for usege
    word = list(word)
    del(word[0])
    del(word[0])
    del(word[len(word)-1])
    word = "".join(word)

#code for the dude
def dude(state):
    """Writes dude to screen"""
    print (" /------")
    if state == 6:
        print (" ")
        print (" ")
        print (" ")
    elif state == 5:
        print (" O")
        print (" ")
        print (" ")
    elif state == 4:
        print (" O")
        print (" |")
        print (" ")
    elif state == 3:
        print(" O")
        print("/|")
        print (" ")
    elif state == 2:
        print(" O")
        print("/|\ ")
        print (" ")
    elif state == 1:
        print(" O")
        print("/|\ ")
        print("/")
    elif state == 0:
        print(" O")
        print("/|\ ")
        print(" /\ ")

#say cmd to make game feel more lifelike                
def say(words):
    time.sleep(0.8)
    print(words)

#intro
say("do you want our random word or do you want to make a word?")
setting = input("(our/own): ")
if setting == "our":
    say ("ok setting word")
elif setting == "own":
    word = input("ok, what word do you want?: ")

say(f"the word is {word} I will now reload the log to for the user")
time.sleep(2)
os.system('cls')
say("hello player, wish you luck")

#variable setup for gameplay loop
state = 6 
guess = []
wl = list(word)
for x in wl:
    guess += "_"
attempt = []

#gameplayloop
while "_" in guess and state >= 1:
    say("ok, so far the word looks like this")
    say(guess)
    say("and the dude looks like this")
    dude(state)
    say ("you have tried these letters") 
    say (attempt)
    say("what is your guess?: ")
    
    letter = input()[0]
    attempt += letter
    for x in range(len(wl)):
        if letter == wl[x]:
            guess[x] = letter
    if letter not in wl:
        state -= 1
        say("oops, sorry thats not in the word.")
        attempt.sort()

#game over dialog
if state <= 0:
    dude(0)
    say("you failed")
else:
    say("good job you did it")

say(f"the word was {word}")
say("reload the program to try again")