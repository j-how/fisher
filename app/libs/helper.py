import re


def is_isbn_or_key(word):
    word = word.replace('-', '')
    prog = re.compile(r'^(\d{13})$|^(\d{10})$')
    if prog.match(word):
        isbn_or_key = 'isbn'
    else:
        isbn_or_key = 'key'

    return isbn_or_key


if __name__ == '__main__':
    print(is_isbn_or_key('99937-0-014-2'))
