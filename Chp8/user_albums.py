def make_album(art_name, title, tracks=None):
    album = {
        'artist': art_name,
        'title': title
    }
    if tracks:
        album['tracks'] = tracks
    return album

while True:
    print("What is the name of the artist?")
    artist = input("Artist: ")

    print("What is the name of the album?")
    nameOfAlbum = input("Album: ")
    
    album = make_album(artist,nameOfAlbum)

    print("Would you like to quit?")

    ans = input("Quit? ")

    if ans == 'q':
        break

    print(album)