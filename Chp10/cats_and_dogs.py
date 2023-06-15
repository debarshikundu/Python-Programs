from pathlib import Path

path1 = Path('/home/debarshi/Desktop/Python-Programs/Chp10/cats.txt')

path2 = Path('/home/debarshi/Desktop/Python-Programs/Chp10/dogs.txt')
try:
    contents1 = path1.read_text()

    contents2 = path2.read_text()

except FileNotFoundError:
    print("File not Found!!!")
else:
    print(contents1)
    print(contents2)