import logging
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QWidget,
                               QMainWindow, QPushButton,
                               QLineEdit, QVBoxLayout, QLabel)
import sys
from src.binary_converter import BinaryConverter

logger = logging.getLogger(__name__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.converter = BinaryConverter()

        self.setWindowTitle('Text Encoder')  # Window Title
        self.label = QLabel(self)
        self.label.setText('Enter string: ')
        self.label.setWordWrap(True)
        self.label.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

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

        logger.info('App layout loaded successfully')

    def btn_clicked(self):
        x = self.converter.user_words_iterator(self.input.text())
        self.label.setText(f'{x['status']} {x['output']}')
        self.label.setWordWrap(True)





# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())
#





