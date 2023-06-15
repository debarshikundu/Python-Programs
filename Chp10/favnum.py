from pathlib import Path
import json 

favnum = input("What is your favorite number?")

path = Path('favnum.json')
contents = json.dumps(favnum)
path.write_text(contents)

print("Thanks! I'll remember that number.")