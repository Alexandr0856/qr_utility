#!/usr/bin/python3

import qrcode


def main():
    data = input('Print data for decoding or word "file" for set path to file decode: ')

    if data == 'file':
        path = input('Write path to file: ')
        
        with open(path) as file:
            data = file.read()
            
    img = qrcode.make(data)
    img.show()

    print('Done')


if __name__ == '__main__':
    main()
