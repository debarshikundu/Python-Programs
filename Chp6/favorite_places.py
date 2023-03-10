favorite_places = {"Arthur":["Sugar Bowl"], "Drew":["Hospital"], "Jimmy":["Basketball Court", "Academic Decathlon", "Band"]}

for k,v in favorite_places.items():
    print(f"\n{k}")
    for value in v:
        print(value)