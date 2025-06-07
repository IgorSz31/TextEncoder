from PySide6.QtWidgets import (QApplication, QWidget,
                               QMainWindow, QPushButton,
                               QLineEdit, QVBoxLayout, QLabel)
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Text Encoder')  # Window Title
        self.label = QLabel(self)

        self.input = QLineEdit(self)
        self.button = QPushButton('Encode')  # Button
        self.button.setCheckable(True)
        self.button.clicked.connect(self.btn_clicked)

        layout = QVBoxLayout() # Vertical Layout
        layout.addWidget(self.input)  #
        layout.addWidget(self.label)  #  Adding all widgets to layout
        layout.addWidget(self.button) #

        container = QWidget(self)
        container.setLayout(layout)

        self.setCentralWidget(container)

    def btn_clicked(self):
        print('hello world')

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())
#





