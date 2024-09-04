import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    symbol = {',', '.', '!', ':', ';', '?'}
    
    if len(text) < size + start:
        return (text[start:], len(text) - start)

    for i in range(size + start - 1, start - 1, -1):
        if text[i] in symbol and text[i+1] not in symbol:
            return (text[start: i + 1], i + 1 - start)



# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as myfile:
        text = myfile.read()

    start = 0
    counter = 1

    while start < len(text):
        fragment = _get_part_text(text, start, PAGE_SIZE)
        word = fragment[0].lstrip()
        book[counter] = word
        start += fragment[1]
        counter += 1      


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))