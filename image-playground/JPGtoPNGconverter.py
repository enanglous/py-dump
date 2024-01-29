import sys
import os
from PIL import Image


def main():
    # grab first and second argument
    image_folder = sys.argv[1]
    output_folder = sys.argv[2]

    # check if new/ exists, if not create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # loop through Pokedex
    for file in os.listdir(image_folder):
        img = Image.open(f'./{image_folder}/{file}')
        clean_name = os.path.splitext(file)[0]
        try:
            img.save(f'./{output_folder}/{clean_name}.png', 'png')
            print('all done!')
        except IOError:
            print('cannot convert', file)


if __name__ == '__main__':
    main()
