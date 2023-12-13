"""
Create a Python file named Midterm-Q2.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

"""
import time
import random
import os
from urllib.request import urlopen

#finds random word
response = urlopen("https://www.mit.edu/~ecprice/wordlist.10000")
txt = response.read()
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
    print (" /------")
    if state == 6:
        print (" ")
    elif state == 5:
        print (" O")
    elif state == 4:
        print (" O")
        print (" |")
    elif state == 3:
        print(" O")
        print("/|")
    elif state == 2:
        print(" O")
        print("/|\ ")
    elif state == 1:
        print(" O")
        print("/|\ ")
        print("/")
    elif state == 0:
        print(" O")
        print("/|\ ")
        print(" /\ ")
                
def say(words):
    time.sleep(2)
    print(words)


say("do you want our word or do you want to make a word?")
setting = input("(our/own)")
if setting == "our":
    say ("ok setting word")
    say(f"the word is {word} I will now reload the log to for the user")
elif setting == "own":
    word = input("ok, what word do you want")

say(f"the word is {word} I will now reload the log to for the user")
#os.system('cls')
state = 6 
guess = []
wl = list(word)
for x in wl:
    guess += "_"
attempt = []

while wl != guess or state > 1:
    say("ok, so far the word looks like this")
    say(guess)
    say("and the dude looks like this")
    dude(state)
    say ("you have tried these letters") 
    say (attempt)
    say("what is your guess")
    
    letter = input()[0]
    attempt += letter
    for x in range(len(wl)):
        if letter == wl[x]:
            guess[x] = letter

    if letter not in wl:
        state -= 1
        say("opss sorry thats not in the word")

if state < 0:
    dude(0)
    say("sorry you failed")
else:
    say("good job you did it")

say(f"the word was {word}")
say("reload the program to try again")