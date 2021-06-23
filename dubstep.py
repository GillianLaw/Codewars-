import re

def song_decoder(song):
    song = re.sub(r"WUB", " ", song)
    tidy = song.strip()
    tidier = re.sub(' +', ' ', tidy)
    return tidier
