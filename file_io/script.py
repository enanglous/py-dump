def main():
    with open('./file_io/test.txt', mode='a') as file:  # 3 modes: r, w, a
        text = file.write('Heyy! It\'s not mee! \n')
        print(text)


if (__name__ == '__main__'):
    main()
