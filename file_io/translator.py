from translate import Translator


def main():
    translator = Translator(to_lang="ja")
    try:
        with open('./file_io/test.txt', mode='r', encoding='utf-8') as my_file:
            text = my_file.read()
            translation = translator.translate(text)
            print(translation)
        with open('./file_io/test-ja.txt', mode='w', encoding='utf-8') as my_file2:
            my_file2.write(translation)
    except FileNotFoundError as err:
        print('File not found')
        raise err
    except IOError as err:
        print('IO Error')
        raise err


if (__name__ == '__main__'):
    main()


# 1. Open file
# 2. Read file
# 3. Translate file
# 4. Write translated text to new file
