from pathlib import Path
import json

path = Path('favnum.json')
contents = path.read_text()
number = json.loads(contents)

print(f"I know your favorite number! It's {number}.")