from src.binary_converter import BinaryConverter

def main():
    converter = BinaryConverter()
    x = converter.user_words_iterator('')
    print(x['status'])

main()