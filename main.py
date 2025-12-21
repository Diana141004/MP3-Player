from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QVBoxLayout, QFrame, QLabel, QSlider, \
    QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MP3 Player")
        self.setFixedSize(600, 600)
        layout = QVBoxLayout()
        lcd_layout = QVBoxLayout()
        buttons_layout = QHBoxLayout()

        lcd_display = QFrame()
        lcd_display.setFrameShape(QFrame.Shape.StyledPanel)
        lcd_display.setFrameShadow(QFrame.Shadow.Sunken)
        lcd_display.setMidLineWidth(3)
        lcd_display.setLineWidth(3)
        lcd_display.setStyleSheet("background: #F8F4EC")

        self.song_name = QLabel("No song loaded")
        self.song_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.song_name.setStyleSheet("color: #FF8FB7; font-family: Consolas; font-size: 20px")

        self.artist = QLabel("No artist specified")
        self.artist.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.artist.setStyleSheet("color: #E83C91; font-family: Consolas; font-size: 15px")

        self.time = QLabel("00:00 / 00:00")
        self.time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time.setStyleSheet("color: #43334C; font-family: Consolas; font-size: 15px")

        lcd_layout.addWidget(self.song_name)
        lcd_layout.addWidget(self.artist)
        lcd_layout.addWidget(self.time)

        lcd_display.setLayout(lcd_layout)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)

        stil_buton = """
            QPushButton {
                background-color: transparent;
                border: none;
                border-radius: 25px;
            }
            QPushButton:hover {
                background-color: #BBB;
                border-radius: 5px; /* Colturi rotunjite la hover */
            }
            QPushButton:pressed {
                background-color: #999;"""


        self.play_button = QPushButton()
        self.play_button.setIcon(QIcon("Icons/play.png"))
        self.play_button.setIconSize(QSize(40,40))
        self.play_button.setStyleSheet(stil_buton)
        self.play_button.setFixedSize(45, 45)
        self.play_button.clicked.connect(self.play_clicked)
        self.play_button.setCheckable(True)

        self.next_button = QPushButton()
        self.next_button.setIcon(QIcon("Icons/next.png"))
        self.next_button.setIconSize(QSize(32, 32))
        self.next_button.setStyleSheet(stil_buton)
        self.next_button.setFixedSize(35, 35)

        self.previous_button = QPushButton()
        self.previous_button.setIcon(QIcon("Icons/previous.png"))
        self.previous_button.setIconSize(QSize(32, 32))
        self.previous_button.setStyleSheet(stil_buton)
        self.previous_button.setFixedSize(35,35)

        buttons_layout.addWidget(self.previous_button)
        buttons_layout.addWidget(self.play_button)
        buttons_layout.addWidget(self.next_button)
        buttons_layout.setSpacing(0)
        buttons_layout.setContentsMargins(100, 0, 100, 0)


        layout.addWidget(lcd_display)
        layout.addSpacing(20)
        layout.addWidget(self.slider)
        layout.addSpacing(20)
        layout.addLayout(buttons_layout)
        layout.setContentsMargins(10,20,10,20)
        # layout.addStretch()

        dummy = QWidget()
        dummy.setLayout(layout)
        self.setCentralWidget(dummy)

    def play_clicked(self, s):
        if s:
            print("Pause")
            self.play_button.setIcon(QIcon("Icons/play.png"))
        else:
            print("Playing")
            self.play_button.setIcon(QIcon("Icons/pause.png"))

app = QApplication([])
window = MainWindow()
window.show()
app.exec()