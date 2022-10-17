from termcolor import colored
with open("words.txt", "r") as f:
    lines = f.readlines()
print(colored('hello', 'red'), colored('world', 'green'))
words = []
lines = [x.replace("*","") for x in lines]
words = [x[-6:-1] for x in lines]
words.pop(-1)
words.pop(561)
print(words)

f.close()
i = open("incomplete.txt","w")
for x in words:
    i.write(x+"\n")