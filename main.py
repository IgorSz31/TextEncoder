import sys
import argparse
import logging
from sys import flags
from src.binary_converter import BinaryConverter
from src.program_status import Status, ErrorMessage
from ui.ui_manager import MainWindow
from logs.logger_config import setup_logger

logger = logging.getLogger(__name__)



def main():
    converter = BinaryConverter()
    x = converter.user_words_iterator(input("Enter a word [ exit() to leave ]: "))
    print(x['status'], x['output'])


if __name__ == "__main__":
    setup_logger()

    parser = argparse.ArgumentParser()
    parser.add_argument('-m','--mode', choices = ['console', 'ui'] ,
                        help='Starts program in command line', default = 'console')
    args = parser.parse_args()

    if args.mode == 'console':
        logger.info('Program opened in console mode')
        while True:
            main()
    elif args.mode == 'ui':
        logger.info('Program opened in UI mode')

        from PySide6.QtWidgets import QApplication
        app = QApplication(sys.argv)
        window = MainWindow()
        window.resize(250, 200)
        window.show()
        sys.exit(app.exec())

    else:
        logger.error(f'Invalid mode: {args.mode} provided')
        print('Invalid mode')
        sys.exit(0)