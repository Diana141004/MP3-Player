from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl

class AudioPlayer:
    def __init__(self):
        # the two engines of this class
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output) #connection between the two engines
        self.audio_output.setVolume(0.7)

    def load_song(self, file_path):
        url = QUrl.fromLocalFile(file_path)
        self.player.setSource(url)

    def play(self):
        self.player.play()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()

    def set_volume(self, volume):
        self.audio_output.setVolume(volume/100)

