from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QVBoxLayout, QFrame, QLabel, QSlider, \
    QHBoxLayout, QListWidget, QStyle, QFileDialog
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from style import stil_list, stil_buton1, stil_buton2, stil_frame
import os
from player_engine import AudioPlayer



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
        self.add_song_button.setFixedSize(60,30)
        self.add_song_button.setStyleSheet(stil_buton2)

        layout_case.addWidget(self.playlist_name, alignment= Qt.AlignmentFlag.AlignLeft)
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

        self.time = QLabel("00:00 / 00:00")
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

        buttons_layout.addWidget(self.previous_button)
        buttons_layout.addWidget(self.play_button)
        buttons_layout.addWidget(self.next_button)
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

        self.play_button.clicked.connect(self.play_clicked)
        self.sound_slider.valueChanged.connect(self.player.set_volume)
        self.sound_slider.valueChanged.connect(self.change_sound_icon)
        self.volume_icon.clicked.connect(self.volume_button_clicked)
        self.songs_list.currentItemChanged.connect(self.song_clicked)
        self.playlist_list.currentItemChanged.connect(self.playlist_clicked)
        self.add_song_button.clicked.connect(self.add_song_clicked)
        self.player.player.durationChanged.connect(self.change_song_duration)
        self.player.player.positionChanged.connect(self.update_song_bar)
        self.time_slider.sliderReleased.connect(self.time_bar_changed)
        self.time_slider.sliderPressed.connect(self.slider_pressed)


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

    def playlist_clicked(self):
        print(self.playlist_list.currentItem().text())
        self.playlist_name.setText(self.playlist_list.currentItem().text())

    def add_song_clicked(self):
        path, _ = QFileDialog.getOpenFileName(self, "Alege Melodia", "", "Audio Files (*.mp3 *.wav *.ogg)")
        if path:
            self.player.load_song(path)
            file_name = os.path.basename(path)
            name = os.path.splitext(file_name)[0]

            self.song_name.setText(name)
            self.artist.setText("Local File")
            self.songs_list.addItem(name)

    def change_song_duration(self, time):
        minutes = time//1000//60
        seconds = (time//1000)%60
        self.time.setText(f"00:00 / {minutes}:{seconds}")

        self.time_slider.setMaximum(time//1000)

    def update_song_bar(self, time_update):
        time = self.player.player.duration()
        minutes = time // 1000 // 60
        seconds = (time // 1000) % 60
        minutes_update = time_update // 1000 // 60
        seconds_update = (time_update // 1000) % 60

        self.time.setText(f"{minutes_update}:{seconds_update} / {minutes}:{seconds}")
        if not self.is_dragging:
            self.time_slider.setValue(time_update // 1000)

    def time_bar_changed(self):
        time_update = self.time_slider.value()*1000
        self.player.player.setPosition(time_update)
        self.is_dragging = False

    def slider_pressed(self):
        self.is_dragging = True

  #------------SOUND & VOLUME-----------------

    def song_clicked(self):
        print(self.songs_list.currentItem().text())
        self.song_name.setText(self.songs_list.currentItem().text())

    def volume_button_clicked(self,s):
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

app = QApplication([])
window = MainWindow()
window.show()
app.exec()