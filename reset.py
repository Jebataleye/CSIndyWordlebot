#colored text just as a test
from termcolor import colored

#opens the uncleaned word list and reads the lines
with open("words.txt", "r") as f:
    lines = f.readlines()

#remove
print(colored('hello', 'red'), colored('world', 'green'))

words = []

#removes the asterisk from some sensitive words
lines = [x.replace("*","") for x in lines]

#adds the last 5 letters of each line to words, those last 5 being the word
words = [x[-6:-1] for x in lines]

#removes the last word and the 562nd word because they're weird
words.pop(-1)
words.pop(561)

#debug print
print(words)

#closes the file
f.close()

#opens the incomplete words file and adds all the words to it
i = open("incomplete.txt","w")
for x in words:
    i.write(x+"\n")
i.close()

#opens the completed file and wipes it
c = open("completed.txt","w")
c.write("")