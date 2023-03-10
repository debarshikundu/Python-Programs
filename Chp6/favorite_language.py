favorite_languages = {
      'jen': ['python', 'rust'],
      'sarah': ['c'],
      'edward': ['rust', 'go'],
      'phil': ['python', 'haskell'],
      'drew': [],
      'phillip': [],
      'jason': [],
      'andrew':[]
      }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    if languages != []:
        for language in languages:
            print(f"\t{language.title()}")
        print(f"{name.title()}, thank you for taking the poll.")
    else:
        print(f"{name.title()}, please take the poll!")
    
    