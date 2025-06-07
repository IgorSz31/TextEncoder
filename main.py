import sys
import argparse
from sys import flags
from src.binary_converter import BinaryConverter
from src.program_status import Status, ErrorMessage
from ui.ui_manager import MainWindow

def main():
    converter = BinaryConverter()
    x = converter.user_words_iterator(input("Enter a word [ exit() to leave ]: "))
    print(x['status'], x['output'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m','--mode', choices = ['console', 'ui'] ,
                        help='Starts program in command line', default = 'console')
    args = parser.parse_args()
    if args.mode == 'console':
        while True:
            main()
    elif args.mode == 'ui':

        from PySide6.QtWidgets import QApplication
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())

    else:
        print('Invalid mode')
        sys.exit(0)