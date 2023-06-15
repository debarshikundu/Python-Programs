from pathlib import Path

"""Absolute or relative path to file..."""
path = Path('/home/debarshi/Desktop/Python-Programs/Chp10/learning_python.txt')
#Reads entire file 
contents = path.read_text()
#prints out entire file
print(contents)
#splits lines into list
lines = contents.splitlines()
#prints each line on a new line
for line in lines: 
    print(line)
    print(line.replace('Python','C')) #Replaces Python with C
