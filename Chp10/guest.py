from pathlib import Path
#Input Name
name = input("What is your name?")
#Output file guest.txt
path = Path('/home/debarshi/Desktop/Python-Programs/Chp10/guest.txt')
#write output to file
path.write_text(name)