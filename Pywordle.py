from curses.ascii import isalpha
import random
from termcolor import colored
with open("incomplete.txt","r") as f:
    lines = f.readlines()
line = random.randint(0,len(lines))
print (line)
word = lines[line]
word = word[:5]
f.close
print(word)
def getguess():
    while True:
        guess = str(input("Enter your guess: "))
        if len(guess)==5 and guess.isalpha():
            return guess
            break
        else:
            print("invalid guess")
        
complete = False
previousguesses = []
c = open("completed.txt","a")
numguess = 1
guessedletters = ""
foundletters = [None,None,None,None,None]
while complete != True:
    guess = getguess()
    print(numguess)
    if numguess == 6:
        print("The word was",word)
        complete = True
        break
    numguess+=1
    coloredguess = ""
    letcolors = [None,None,None,None,None]
    word = word.lower()
    if guess == word.lower():
        print("yay")
        letcolors = ["green" for x in letcolors]
        complete = True
    else:
        for place in range(5):
            if guess[place] == word[place]:
                foundletters[place] = [word[place],"g"]
                letcolors[place] = "green"
            elif guess[place] in word:
                foundletters[place] = [word[place],"y"]
                letcolors[place] = "yellow"
            else:
                letcolors[place] = "grey"
    for g in previousguesses:
        print(colored(g[0][0],g[1][0]),colored(g[0][1],g[1][1]),colored(g[0][2],g[1][2]),colored(g[0][3],g[1][3]),colored(g[0][4],g[1][4]))
    print(colored(guess[0],letcolors[0]),colored(guess[1],letcolors[1]),colored(guess[2],letcolors[2]),colored(guess[3],letcolors[3]),colored(guess[4],letcolors[4]))
    previousguesses.append([guess,letcolors])
    for let in guess:
        if let not in guessedletters:
            guessedletters+=let
    c.write(numguess+"-"+guessedletters+"-")
f = open("incomplete.txt","w")


lines.pop(line)
for x in lines:
    f.write(x)
