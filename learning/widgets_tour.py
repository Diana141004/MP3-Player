import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDial,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

# # ----------------LABEL-------------------
#         widget = QLabel("Hello")
#         # font = widget.font() #making a font object
#         # font.setPointSize(30) #setting the font with the object font
#         # widget.setFont(font)
#         # widget.setAlignment(
#         #     Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
#         # )
#
#         #widget.setFont(QFont("Arial", 30)), need to import QFont class
#         widget.setPixmap(QPixmap("cat.webp"))
#         widget.setScaledContents(True)

# # ----------------Checkbox-------------------
#         widget = QCheckBox("This is a checkbox")
#         widget.setCheckState(Qt.CheckState.Checked)
#
#         # For tristate: widget.setCheckState(Qt.CheckState.PartiallyChecked)
#         widget.setTristate(True)# or for tristate
#         widget.stateChanged.connect(self.show_state)
#
#         self.setCentralWidget(widget)
#
#     def show_state(self, s):
#         print(s == Qt.CheckState.Checked.value)
#         print(s)
# # ----------------QComboBox-------------------

    #     widget = QComboBox()
    #     widget.addItems(["One", "Two", "Three"])
    #
    #     # Sends the current index (position) of the selected item.
    #     widget.currentIndexChanged.connect(self.index_changed)
    #
    #     # There is an alternate signal to send the text.
    #     widget.currentTextChanged.connect(self.text_changed)
    #     widget.setEditable(True)
    #
    #     widget.setInsertPolicy(widget.InsertPolicy.NoInsert)
    #
    #     self.setCentralWidget(widget)
    #
    # def index_changed(self, i):  # i is an int
    #     print(i)
    #
    # def text_changed(self, s):  # s is a str
    #     print(s)

# # ----------------QListWidget-------------------
#         widget = QListWidget()
#         widget.addItems(["One", "Two", "Three"])
#
#         widget.currentItemChanged.connect(self.index_changed)
#         widget.currentTextChanged.connect(self.text_changed)
#
#         self.setCentralWidget(widget)
#
#     def index_changed(self, i):  # Not an index, i is a QListWidgetItem
#         print(i.text())
#
#     def text_changed(self, s):  # s is a str
#         print(s)

# # ----------------QLineEdit-------------------
#         widget = QLineEdit()
#         widget.setMaxLength(10)
#         widget.setPlaceholderText("Enter your text")
#
#         # widget.setReadOnly(True) # uncomment this to make readonly
#
#         widget.returnPressed.connect(self.return_pressed)
#         widget.selectionChanged.connect(self.selection_changed)
#         widget.textChanged.connect(self.text_changed)
#         widget.textEdited.connect(self.text_edited)
#
#         self.setCentralWidget(widget)
#
#     def return_pressed(self):
#         print("Return pressed!")
#         self.centralWidget().setText("BOOM!")
#
#     def selection_changed(self):
#         print("Selection changed")
#         print(self.centralWidget().selectedText())
#
#     def text_changed(self, s):
#         print("Text changed...")
#         print(s)
#
#     def text_edited(self, s):
#         print("Text edited...")
#         print(s)

# # ----------------QSpinBox and QDoubleSpinBox-------------------

    #     widget = QSpinBox()
    #     # Or: widget = QDoubleSpinBox()
    #
    #     widget.setMinimum(-9)
    #     widget.setMaximum(3)
    #     # Or: widget.setRange(-9, 3)
    #
    #     widget.setPrefix("$")
    #     widget.setSuffix("c")
    #     widget.setSingleStep(3)  # Or e.g. 3.0 for QDoubleSpinBox
    #     widget.valueChanged.connect(self.value_changed)
    #     widget.textChanged.connect(self.value_changed_str)
    #
    #     self.setCentralWidget(widget)
    #
    # def value_changed(self, i):
    #     print(i)
    #
    # def value_changed_str(self, s):
    #     print(s)

# # ----------------QSlider-------------------

    #     # widget = QSlider()
    #     widget = QSlider(Qt.Orientation.Horizontal)
    #
    #     widget.setMinimum(-10)
    #     widget.setMaximum(3)
    #     # Or: widget.setRange(-10,3)
    #
    #     widget.setSingleStep(3)
    #
    #     widget.valueChanged.connect(self.value_changed)
    #     widget.sliderMoved.connect(self.slider_position)
    #     widget.sliderPressed.connect(self.slider_pressed)
    #     widget.sliderReleased.connect(self.slider_released)
    #
    #     self.setCentralWidget(widget)
    #
    # def value_changed(self, i):
    #     print(i)
    #
    # def slider_position(self, p):
    #     print("Position", p)
    #
    # def slider_pressed(self):
    #     print("Pressed!")
    #
    # def slider_released(self):
    #     print("Released")

# # ----------------QDial-------------------

        widget = QDial()
        widget.setRange(-10, 100)
        widget.setSingleStep(1)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print("position", p)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()