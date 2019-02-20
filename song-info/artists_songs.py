import os
import sys

class MusicFile:

    metadata_path = ''
    artist_songs = dict()
    songs = []

    def __init__(self, path):
        self.metadata_path = path
        self.read_file()

    def read_file(self):
        try:
            file_obj = open(self.metadata_path, 'r')
            for line in file_obj:
                artist, song = line.rstrip().split(' - ')
                if artist in self.artist_songs:
                    self.artist_songs[artist].append(song)
                else:
                    self.artist_songs[artist] = [song]
        except Exception as e:
            print(e)
            sys.exit(1)

    def artist(self, artist):
        if artist in self.artist_songs:
            self.songs = '\n'.join(self.artist_songs[artist])
        else:
            self.songs = 'No information available about the artist'
        return self


current_dir = os.path.dirname(os.path.realpath(__file__))
music = MusicFile(current_dir + '/metadata.txt')
print(music.artist('Joy Division').songs)