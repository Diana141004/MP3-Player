from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QVBoxLayout, QFrame, QLabel, QSlider, \
    QHBoxLayout, QListWidget, QStyle, QFileDialog, QInputDialog, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from style import stil_list, stil_buton1, stil_buton2, stil_frame, stil_button_toggle
import os
import json
from player_engine import AudioPlayer
import random



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    #-----------------UI---------------

        self.setWindowTitle("MP3 Player")
        self.setFixedSize(1200, 700)
        layout = QHBoxLayout()
        layout_left = QVBoxLayout()
        layout_right = QVBoxLayout()

#LEFT
        left_frame = QFrame()
        left_frame.setFrameShape(QFrame.Shape.StyledPanel)
        left_frame.setFrameShadow(QFrame.Shadow.Sunken)
        left_frame.setMidLineWidth(3)
        left_frame.setLineWidth(3)
        left_frame.setStyleSheet(stil_frame)

        self.button_playlist = QPushButton("Create Playlist")
        self.button_playlist.setFixedSize(120,32)
        self.button_playlist.setStyleSheet(stil_buton2)

        label_playlist = QLabel("Playlists")
        label_playlist.setStyleSheet("color: #FDB5CE; font-family; Consolas; font-size: 20px")

        self.playlist_list = QListWidget()
        self.playlist_list.setStyleSheet(stil_list)
        # self.playlist_list.addItems(["Playlist1", "Playlist2", "Playlist4", "Playlist5", "Playlist6", "Playlist7", "Playlist8", "Playlist9", "Playlist10", "Playlist11", "Playlist12", "Playlist13", "Playlist14", "Playlist15", "Playlist16", "Playlist17", "Playlist18", "Playlist19", "Playlist20", "Playlist21", "Playlist22", "Playlist23", "Playlist24", "Playlist25"])

        layout_frame1 = QVBoxLayout()
        layout_frame1.addWidget(self.button_playlist, alignment= Qt.AlignmentFlag.AlignCenter)
        layout_frame1.addWidget(label_playlist, alignment= Qt.AlignmentFlag.AlignCenter)
        layout_frame1.addWidget(self.playlist_list)

        left_frame.setLayout(layout_frame1)
        layout_left.addWidget(left_frame)

#RIGHT
    #TOP
        layout_right_up = QVBoxLayout() #layout for the right up part of the screen
        layout_case = QHBoxLayout() #to connect the Playlist name label and the button
        right_frame = QFrame()
        right_frame.setFrameShape(QFrame.Shape.StyledPanel)
        right_frame.setFrameShadow(QFrame.Shadow.Sunken)
        right_frame.setMidLineWidth(3)
        right_frame.setLineWidth(3)
        right_frame.setStyleSheet(stil_frame)

        self.playlist_name = QLabel("Playlist Name")
        self.playlist_name.setStyleSheet("color: #FDB5CE; font-family; Consolas; font-size: 20px")

        self.add_song_button = QPushButton("Add Song")
        self.add_song_button.setFixedSize(80,30)
        self.add_song_button.setStyleSheet(stil_buton2)

        self.delete_song_button = QPushButton("Delete Song")
        self.delete_song_button.setFixedSize(80, 30)
        self.delete_song_button.setStyleSheet(stil_buton2)

        layout_case.addWidget(self.playlist_name, alignment= Qt.AlignmentFlag.AlignLeft)
        layout_case.addStretch()
        layout_case.addWidget(self.delete_song_button, alignment=Qt.AlignmentFlag.AlignRight)
        layout_case.addWidget(self.add_song_button, alignment=Qt.AlignmentFlag.AlignRight)

        self.songs_list = QListWidget()
        self.songs_list.setStyleSheet(stil_list)
        # self.songs_list.addItems(
        #     ["Song1", "Song2", "Song4", "Song5", "Song6", "Song7", "Song8", "Song9",
        #      "Song10", "Song11"])

        layout_frame2 = QVBoxLayout()
        layout_frame2.addLayout(layout_case)
        layout_frame2.addWidget(self.songs_list)
        right_frame.setLayout(layout_frame2)

        layout_right_up.addWidget(right_frame)

        lcd_layout = QVBoxLayout()
        buttons_layout = QHBoxLayout()

    #BOTTOM
        lcd_display = QFrame()
        lcd_display.setFrameShape(QFrame.Shape.StyledPanel)
        lcd_display.setFrameShadow(QFrame.Shadow.Sunken)
        lcd_display.setMidLineWidth(3)
        lcd_display.setLineWidth(3)
        lcd_display.setStyleSheet(stil_frame)

        self.song_name = QLabel("No song loaded")
        self.song_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.song_name.setStyleSheet("color: #FF8FB7; font-family: Consolas; font-size: 20px")
        self.song_name.setContentsMargins(25,0,0,0)

        self.sound_slider = QSlider(Qt.Orientation.Horizontal)
        self.sound_slider.setMinimum(0)
        self.sound_slider.setMaximum(100)

        self.volume_icon = QPushButton()
        self.volume_icon.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaVolume))
        self.volume_icon.setStyleSheet(stil_buton1)
        self.volume_icon.setFlat(True)
        self.volume_icon.setCheckable(True)

        layout_box = QHBoxLayout()
        layout_box.addWidget(self.song_name, 4 ,alignment= Qt.AlignmentFlag.AlignCenter)
        layout_box.addWidget(self.volume_icon)
        layout_box.addWidget(self.sound_slider,1)
        layout_box.setContentsMargins(155,0,0,0)


        self.artist = QLabel("No artist specified")
        self.artist.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.artist.setStyleSheet("color: #C9B59C; font-family: Consolas; font-size: 15px")

        self.time = QLabel("0:00 / 0:00")
        self.time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time.setStyleSheet("color: #43334C; font-family: Consolas; font-size: 15px")

        self.time_slider = QSlider(Qt.Orientation.Horizontal)
        self.time_slider.setMinimum(0)
        self.time_slider.setMaximum(100)

        self.play_button = QPushButton()
        self.play_button.setIcon(QIcon("Icons/play.png"))
        self.play_button.setIconSize(QSize(80,80))
        self.play_button.setStyleSheet(stil_buton1)
        self.play_button.setFixedSize(80, 80)
        self.play_button.setCheckable(True)

        self.next_button = QPushButton()
        self.next_button.setIcon(QIcon("Icons/next.png"))
        self.next_button.setIconSize(QSize(60, 60))
        self.next_button.setStyleSheet(stil_buton1)
        self.next_button.setFixedSize(60, 60)

        self.previous_button = QPushButton()
        self.previous_button.setIcon(QIcon("Icons/previous.png"))
        self.previous_button.setIconSize(QSize(60, 60))
        self.previous_button.setStyleSheet(stil_buton1)
        self.previous_button.setFixedSize(60, 60)

        self.shuffle_button = QPushButton()
        self.shuffle_button.setIcon(QIcon("Icons/shuffle.png"))
        self.shuffle_button.setIconSize(QSize(60, 60))
        self.shuffle_button.setStyleSheet(stil_button_toggle)
        self.shuffle_button.setFixedSize(60, 60)
        self.shuffle_button.setCheckable(True)

        self.repeat_button = QPushButton()
        self.repeat_button.setIcon(QIcon("Icons/repeat.png"))
        self.repeat_button.setIconSize(QSize(60, 60))
        self.repeat_button.setStyleSheet(stil_button_toggle)
        self.repeat_button.setFixedSize(60, 60)
        self.repeat_button.setCheckable(True)

        buttons_layout.addWidget(self.shuffle_button)
        buttons_layout.addWidget(self.previous_button)
        buttons_layout.addWidget(self.play_button)
        buttons_layout.addWidget(self.next_button)
        buttons_layout.addWidget(self.repeat_button)
        buttons_layout.setSpacing(0)
        buttons_layout.setContentsMargins(100, 0, 100, 0)

        lcd_layout.addLayout(layout_box)
        lcd_layout.addWidget(self.artist)
        lcd_layout.addWidget(self.time)
        lcd_layout.addWidget(self.time_slider)
        lcd_layout.addLayout(buttons_layout)

        lcd_display.setLayout(lcd_layout)


        layout_right_down = QVBoxLayout()
        layout_right_down.addWidget(lcd_display)
        # layout_right_down.addSpacing(20)
        # layout_right_down.addWidget(self.slider)
        # layout_right_down.addSpacing(20)
        # layout_right_down.addLayout(buttons_layout)
        # layout_right_down.setContentsMargins(10,20,10,20)

        layout_right.addLayout(layout_right_up,2)
        layout_right.addLayout(layout_right_down,1)

        layout.addLayout(layout_left,1)
        layout.addLayout(layout_right,4)


        dummy = QWidget()
        dummy.setLayout(layout)
        self.setCentralWidget(dummy)


    #-----------------BACKEND----------------------------

        self.player = AudioPlayer()
        self.sound_slider.setValue(70)
        self.is_dragging = False
        self.songs = []
        self.current_index = 0
        self.shuffled_songs = []
        self.shuffle_index = 0
        self.all_playlists = {}

        self.play_button.clicked.connect(self.play_clicked)
        self.next_button.clicked.connect(self.next_clicked)
        self.previous_button.clicked.connect(self.previous_clicked)
        self.sound_slider.valueChanged.connect(self.player.set_volume)
        self.sound_slider.valueChanged.connect(self.change_sound_icon)
        self.volume_icon.clicked.connect(self.volume_button_clicked)
        self.songs_list.currentItemChanged.connect(self.song_clicked)
        self.playlist_list.currentItemChanged.connect(self.playlist_clicked)
        self.add_song_button.clicked.connect(self.add_song_clicked)
        self.delete_song_button.clicked.connect(self.delete_song_clicked)
        self.player.player.durationChanged.connect(self.change_song_duration)
        self.player.player.positionChanged.connect(self.update_song_bar)
        self.time_slider.sliderReleased.connect(self.time_bar_changed)
        self.time_slider.sliderPressed.connect(self.slider_pressed)
        self.button_playlist.clicked.connect(self.create_playlist_clicked)
        self.repeat_button.clicked.connect(self.repeat_clicked)
        self.shuffle_button.clicked.connect(self.shuffle_clicked)

        self.load_playlists()


    #------------------FUNCTIONS-------------------

    def play_clicked(self, s):
        if s:
            print("Playing")
            self.player.play()
            self.play_button.setIcon(QIcon("Icons/pause.png"))
        else:
            print("Pause")
            self.player.pause()
            self.play_button.setIcon(QIcon("Icons/play.png"))

    def next_clicked(self):

        if self.repeat_button.isChecked():
            self.player.load_song(self.songs[self.current_index])
            self.play_clicked(True)
            self.play_button.setChecked(True)
            self.songs_list.setCurrentRow(self.current_index)
            return

        if self.shuffle_button.isChecked():
            if self.shuffle_index == len(self.shuffled_songs) - 1:
                self.shuffle_index = 0
            else:
                self.shuffle_index += 1

            current = self.shuffled_songs[self.shuffle_index]
            self.current_index = self.songs.index(current)
            self.player.load_song(current)

        else:

            if self.current_index == len(self.songs) - 1:
                self.current_index = 0
            else:
                self.current_index += 1

            self.player.load_song(self.songs[self.current_index])

        self.play_clicked(True)
        self.play_button.setChecked(True)
        self.songs_list.setCurrentRow(self.current_index)

    def previous_clicked(self):
        if self.repeat_button.isChecked():
            self.player.load_song(self.songs[self.current_index])
            self.play_clicked(True)
            self.play_button.setChecked(True)
            return

        if self.shuffle_button.isChecked():
            if self.shuffle_index == 0:
                self.shuffle_index = len(self.shuffled_songs) - 1
            else:
                self.shuffle_index -= 1

            current = self.shuffled_songs[self.shuffle_index]
            self.current_index = self.songs.index(current)
            self.player.load_song(current)

        else:

            if self.current_index == 0:
                self.current_index = len(self.songs) - 1
            else:
                self.current_index -= 1
            self.player.load_song(self.songs[self.current_index])

        self.play_clicked(True)
        self.play_button.setChecked(True)
        self.songs_list.setCurrentRow(self.current_index)

    def repeat_clicked(self):
        if self.repeat_button.isChecked():
            print("repeat active")
        else:
            print("repeat inactive")

    def shuffle_clicked(self):
        if self.shuffle_button.isChecked():

            self.shuffled_songs = self.songs.copy()
            random.shuffle(self.shuffled_songs)
            print("shuffle active")

            if self.songs:
                current = self.songs[self.current_index]
                self.shuffled_songs.remove(current)
                self.shuffled_songs.insert(0,current)
                self.shuffle_index = 0

        else:
            print("shuffle inactive")
            current = self.shuffled_songs[self.shuffle_index]
            self.current_index = self.songs.index(current)

    def change_song_duration(self, time):
        minutes = time//1000//60
        seconds = (time//1000)%60
        self.time.setText(f"0:00 / {minutes}:{seconds}")

        self.time_slider.setMaximum(time//1000)

    def update_song_bar(self, time_update):
        time = self.player.player.duration()
        minutes = time // 1000 // 60
        seconds = (time // 1000) % 60
        minutes_update = time_update // 1000 // 60
        seconds_update = (time_update // 1000) % 60

        if seconds < 10:
            seconds = f"0{seconds}"

        if seconds_update < 10:
            seconds_update = f"0{seconds_update}"

        self.time.setText(f"{minutes_update}:{seconds_update} / {minutes}:{seconds}")
        if not self.is_dragging:
            self.time_slider.setValue(time_update // 1000)

        if time == time_update:
            self.next_clicked()

    def time_bar_changed(self):
        time_update = self.time_slider.value()*1000
        self.player.player.setPosition(time_update)
        self.is_dragging = False

    def slider_pressed(self):
        self.is_dragging = True

  #------------SOUND & VOLUME-----------------

    def volume_button_clicked(self, s):
        if s:
            print("Mute")
            self.player.set_volume(0)
            self.volume_icon.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaVolumeMuted))
            self.sound_slider.setValue(0)
        else:
            print("Unmute")
            self.player.set_volume(70)
            self.volume_icon.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaVolume))
            self.sound_slider.setValue(70)

    def change_sound_icon(self):
        if self.sound_slider.value() != 0:
            self.volume_icon.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaVolume))
        else:
            self.volume_icon.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaVolumeMuted))

#--------- SONGS AND PLAYLISTS ------------

    def playlist_clicked(self):
        print(self.playlist_list.currentItem().text())
        self.playlist_name.setText(self.playlist_list.currentItem().text())
        self.songs_list.clear()
        self.songs = []
        current_playlist = self.all_playlists[self.playlist_name.text()]
        for song in current_playlist:
            file_name = os.path.basename(song)
            name = os.path.splitext(file_name)[0]
            self.songs_list.addItem(name)
            self.songs.append(song)

    def add_song_clicked(self):
        path, _ = QFileDialog.getOpenFileName(self, "Alege Melodia", "", "Audio Files (*.mp3 *.wav *.ogg)")
        if path:
            self.player.load_song(path)
            file_name = os.path.basename(path)
            name = os.path.splitext(file_name)[0]
            self.songs.append(path)

            self.song_name.setText(name)
            self.artist.setText("Local File")
            self.songs_list.addItem(name)
            self.save_playlist_to_file()

    def delete_song_clicked(self):
        row = self.songs_list.currentRow()
        if  row < 0:
            return

        self.songs_list.blockSignals(True)

        self.player.pause()
        self.song_name.setText("No song loaded")
        self.current_index = 0
        self.time.setText(f"0:00 / 0:00")

        if self.shuffle_button.isChecked():
            current = self.songs[row]
            self.shuffled_songs.remove(current)

        self.songs.pop(row)
        self.songs_list.takeItem(row)
        self.save_playlist_to_file()

        self.songs_list.blockSignals(False)


    def create_playlist_clicked(self):
        name, ok = QInputDialog.getText(self, "Playlist Nou", "Introdu numele playlist-ului:")
        if ok and name:
            if name in self.all_playlists:
                QMessageBox.warning(self, "Eroare", "Acest playlist există deja!")
                return
            self.all_playlists[name] = []
            self.playlist_list.addItem(name)
            self.save_playlist_to_file()
            print(f"Playlist-ul {name} a fost creat!")


    def song_clicked(self):
        if self.songs_list.currentRow() < 0 or self.songs_list.currentItem() is None:
            return

        print(self.songs_list.currentItem().text())
        self.song_name.setText(self.songs_list.currentItem().text())
        self.current_index = self.songs_list.currentRow()
        self.player.load_song(self.songs[self.current_index])
        self.play_clicked(True)
        self.play_button.setChecked(True)


    def save_playlist_to_file(self):
        self.all_playlists[self.playlist_name.text()] = self.songs

        with open("playlist_data.json", "w") as file:
            json.dump(self.all_playlists, file, indent = 4)

    def load_playlists(self):
        if os.path.exists("playlist_data.json"):
            with open("playlist_data.json", "r") as file:
                data = json.load(file)
                self.all_playlists = data

        for playlist in self.all_playlists:
            self.playlist_list.addItem(playlist)

        if self.playlist_list.count() > 0:
            self.playlist_list.setCurrentRow(0)
            self.playlist_clicked()


app = QApplication([])
window = MainWindow()
window.show()
app.exec()