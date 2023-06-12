def make_album(art_name, title, tracks=None):
    album = {
        'artist': art_name,
        'title': title
    }
    if tracks:
        album['tracks'] = tracks
    return album

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('willie nelson', 'red-headed stranger')
print(album)

album = make_album('iron maiden', 'piece of mind', tracks=8)
print(album)




