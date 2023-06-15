from pathlib import Path
"""Silent version- Fails quietly if file not found!!!"""
path1 = Path('/home/debarshi/Desktop/Python-Programs/Chp10/cats.txt')

path2 = Path('/home/debarshi/Desktop/Python-Programs/Chp10/dogs.txt')
try:
    contents1 = path1.read_text()

    contents2 = path2.read_text()

except FileNotFoundError:
    print("")
else:
    print(contents1)
    print(contents2)