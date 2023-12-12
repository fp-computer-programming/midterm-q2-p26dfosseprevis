"""
Create a Python file named Midterm-Q2.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

"""
import time
import random
import os
from urllib.request import urlopen

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = urlopen(word_site)
txt = response.read()
WORDS = txt.splitlines()
word = random.choice(WORDS)

print(word)
def dude(state):
    print (" /------")
    if state == 0:
        print (" ")
    elif state == 1:
        print (" O")
    elif state == 2:
        print (" O")
        print (" |")
    elif state == 3:
        print(" O")
        print("/|")
    elif state == 4:
        print(" O")
        print("/|\ ")
    elif state == 5:
        print(" O")
        print("/|\ ")
        print("/")
    elif state == 6:
        print(" O")
        print("/|\ ")
        print(" /\ ")
                
def say(words):
    print(words)
    time.sleep(3)        
        
say("do you want our word or do you want to make a word?")
setting = input("(our/own)")
if setting == "our":
    say ("ok setting word")
    say(f"")
elif setting == "own":
    word = input("ok, what word do you want")


    

