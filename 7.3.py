class Song:

    def __init__(self, title, singer, musician, genre):
        self.title = title
        self.singer = singer
        self.musician = musician
        self.genre = genre


class JukeBox:

    def __init__(self):
        self.currently_playing = None
        self.songs_queue = []
        self.songs = []
        self.playlist = {}  # name is key and list of songs as value
        self.favorites = []

    def add_song(self, song):
        pass

    def remove_song(self, song):
        pass

    def add_playlist(self, playlist, songs):
        pass

    def remove_playlist(self, playlist):
        pass

    def add_to_playlist(self, playlist, song):
        pass

    def remove_from_playlist(self, playlist, song):
        pass

    def add_song_to_queue(self, song):
        pass

    def remove_song_from_queue(self, song):
        pass

    def add_song_to_favorite(self, song):
        pass

    def remove_song_from_remove(self, song):
        pass

    def shuffle(self):
        pass

    def play(self, song):
        pass

    def play_queue(self):
        pass

    def play_playlist(self, playlist):
        pass

    def repeat_one(self):
        pass

    def repeat_all(self):
        pass

    def pause(self):
        pass

    def stop(self):
        pass

    def forward(self):
        pass

    def backward(self):
        pass

    def next_song(self):
        pass

    def prev_song(self):
        pass

    def increase_volume(self):
        pass

    def decrease_volume(self):
        pass


def main():
    jukebox = JukeBox()


if __name__ == '__main__':
    main()
