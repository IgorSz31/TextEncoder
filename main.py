import sys
import argparse
from src.binary_converter import BinaryConverter


def main():
    converter = BinaryConverter()
    x = converter.user_words_iterator(input("Enter a word: "))
    print(x['status'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m','--mode', choices = ['console', 'ui'] ,
                        help='Starts program in command line', default = 'console')
    args = parser.parse_args()
    if args.mode == 'console':
        main()
    elif args.mode == 'ui':
        print('--- PLACE HOLDER ---')
    else:
        print('Invalid mode')
        sys.exit(0)