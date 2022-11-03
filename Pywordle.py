import random
from turtle import pos
#colored text
from termcolor import colored
#opens the list of possible wordle words
with open("incomplete.txt","r") as f:
    lines = f.readlines()

#picks a random word and cleans it up
line = random.randint(0,len(lines))
#print (line)
word = lines[line]
word = word[:5]
f.close()
#prints the word (for debugging)
#print(word)
p = open("possibleguesses.txt","r")
possibleguesses = p.readlines()
for ind in range(len(possibleguesses)):
    possibleguesses[ind] = possibleguesses[ind].replace("\n","")

#makes sure that the users guess is valid (doesn't check if the guess is a real word like regular wordle)
def getguess():
    while True:
        guess = str(input("Enter your guess: "))
        if len(guess)==5 and guess.isalpha() and guess.lower() in possibleguesses:
            return guess
            break
        else:
            print("invalid guess")

#variable used for the game run loop        
complete = False

#list that holds the previous guesses and their letter colors
previousguesses = []

#opens the file holding completed guesses
c = open("completed.txt","a")

#counts how many guesses the user has made
numguess = 1

#A string of all guessed letters
guessedletters = ""

#stores the colors for each letter to be printed
greenletters = [None,None,None,None,None]
yellowletters = [None,None,None,None,None]

#runs until you run out of guesses or guess the word
while complete != True:
    #guess input
    guess = getguess()

    #writes the user's guess to the completed file along with: which guess they were on, what letters they had guessed, which letters were green and yellow, and their guess
    c.write(str(numguess)+"-"+guessedletters+"-"+str(greenletters[0])+"-"+str(greenletters[1])+"-"+str(greenletters[2])+"-"+str(greenletters[3])+"-"+str(greenletters[4])+"-"+str(yellowletters[0])+"-"+str(yellowletters[1])+"-"+str(yellowletters[2])+"-"+str(yellowletters[3])+"-"+str(yellowletters[4])+"-"+guess+"\n")
    
    #debug prints which guess the user is on
    #print(numguess)

    #stores which colors each letter should be
    letcolors = [None,None,None,None,None]

    #lower cases the word
    word = word.lower()

    #checks if the user guessed correctly and breaks the loop
    if guess == word.lower():
        print("yay")
        letcolors = ["green" for x in letcolors]
        complete = True
        break
    else:
        #goes through each letter of the guess and sees if its a match, if the letter is in the word, or its neither
        for place in range(5):
            #checks for a letter match
            if guess[place] == word[place]:
                #stores the matched letter to the corresponding place in greenletters
                greenletters[place] = word[place]
                #says that that letters color should be green when printed
                letcolors[place] = "green"
            #checks if letter is in the word
            elif guess[place] in word:
                #stores the matched letter to the corresponding place in green letters:
                if yellowletters[place] != None and guess[place] not in yellowletters[place]:
                    yellowletters[place] += guess[place]
                else:
                    yellowletters[place] = guess[place]
                #says that that letters color should be yellow when printed
                letcolors[place] = "yellow"
            else:
                #says that that letter's color should be gray when printed
                letcolors[place] = "grey"
    
    
    
    
    #prints each of the previous guesses and their colors
    for g in previousguesses:
        print(colored(g[0][0],g[1][0]),colored(g[0][1],g[1][1]),colored(g[0][2],g[1][2]),colored(g[0][3],g[1][3]),colored(g[0][4],g[1][4]))
    
    #prints the current guess and its colors
    print(colored(guess[0],letcolors[0]),colored(guess[1],letcolors[1]),colored(guess[2],letcolors[2]),colored(guess[3],letcolors[3]),colored(guess[4],letcolors[4]))
    
    #checks if you ran out of guesses
    if numguess == 6:
        print("The word was",word)
        complete = True
        break
    #adds the current guess to the previous guesses
    previousguesses.append([guess,letcolors])

    #adds newly guessed letters to the total guessed letters
    for let in guess:
        if let not in guessedletters:
            guessedletters+=let
    #debug prints the green and yellow letters
    #print(greenletters)
    #print(yellowletters)
    
    #debug prints the data sent to the txt file
    #print(str(numguess)+"-"+guessedletters+"-"+str(greenletters[0])+"-"+str(greenletters[1])+"-"+str(greenletters[2])+"-"+str(greenletters[3])+"-"+str(greenletters[4])+"-"+str(yellowletters[0])+"-"+str(yellowletters[1])+"-"+str(yellowletters[2])+"-"+str(yellowletters[3])+"-"+str(yellowletters[4])+"-"+guess)
    
    #adds 1 to the total number of guesses
    numguess+=1

#closes the compelted file
c.close()

#opens the incomplete file
f = open("incomplete.txt","w")

#removes the guesses word from the list to remove repeats
lines.pop(line)

#rewrites the file without the guessed word
for x in lines:
    f.write(x)
