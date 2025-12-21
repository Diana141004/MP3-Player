import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        layout = QGridLayout()
        stacked_layout = QStackedLayout()

        stacked_layout.addWidget(Color("red"))
        stacked_layout.addWidget(Color("purple"))
        stacked_layout.addWidget(Color("yellow"))
        stacked_layout.addWidget(Color("brown"))
        stacked_layout.setCurrentIndex(3)


        layout2.addWidget(Color("pink"))
        layout2.addWidget(Color("white"))
        layout2.addWidget(Color("magenta"))

        layout1.addLayout(layout2)
        layout1.addWidget(Color("green"))

        layout3.addWidget(Color("red"))
        layout3.addWidget(Color("orange"))

        layout1.addLayout(layout3)
        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(0)

        layout.addWidget(Color("dark red"), 0, 3)
        layout.addLayout(layout1, 2,2)
        layout.addWidget(Color("yellow"), 3, 0)

        widget = QWidget()#dummy widget because i cant how directly the layout on the screen
        widget.setLayout(stacked_layout) #setting the layout
        self.setCentralWidget(widget) #setting the widget that contains the layout as central widget

        # widget = Color("red")
        # self.setCentralWidget(widget)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()