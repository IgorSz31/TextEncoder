import argparse
from src.binary_converter import BinaryConverter


def main():
    converter = BinaryConverter()
    x = converter.user_words_iterator(input("Enter a word: "))
    print(x['status'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('start_program', help='Starts program in command line')
    args = parser.parse_args()
    if args.start_program == 'console'.lower():
        main()
    elif args.start_program == 'ui'.lower():
        print('--- PLACE HOLDER ---')
