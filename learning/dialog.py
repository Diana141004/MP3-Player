import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, \
    QWidget, QMessageBox

class CustomDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("HELLO!")

        QBtn = (
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        layout = QVBoxLayout()

        button_dialog = QPushButton("Press me for a dialog!")
        button_dialog.clicked.connect(self.button_d_clicked)

        button_message = QPushButton("Press me for a message!")
        button_message.clicked.connect(self.button_m_clicked)

        layout.addWidget(button_dialog)
        layout.addWidget(button_message)

        dummy = QWidget()
        dummy.setLayout(layout)
        self.setCentralWidget(dummy)

    def button_d_clicked(self, s):
        print("click", s)

        dialog = CustomDialog(self)
        if dialog.exec():
            print("Success!")
        else:
            print("Cancel!")

    def button_m_clicked(self, s):
        print("click", s)

        # dialog = QMessageBox(self)
        # dialog.setWindowTitle("I have a question!")
        # dialog.setText("This is a simple dialog")
        # dialog.setIcon(QMessageBox.Icon.Question)
        # button = dialog.exec()
        #
        # if button == QMessageBox.StandardButton.Ok:
        #     print("OK!")

        #quicker method
        button = QMessageBox.question(
            self, "Question dialog", "The longer message"
        )

        if button == QMessageBox.StandardButton.Yes:
            print("YES!")
        else:
            print("NO!")





app = QApplication([])
window = MainWindow()
window.show()
app.exec()