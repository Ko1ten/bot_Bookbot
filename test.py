def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    symbol = {',', '.', '!', ':', ';', '?'}

    if len(text) < size + start:
        return (text[start:], len(text) - start)

    for i in range(size + start - 1, start - 1, -1):
        if text[i] in symbol and text[i+1] not in symbol:
            return (text[start: i + 1], i + 1 - start)



text = 'Да? Вы точно уверены? Может быть, вам это показалось?.. Ну, хорошо, приходите завтра, тогда и посмотрим, что можно сделать. И никаких возражений! Завтра, значит, завтра!'
print(*_get_part_text(text, 0, 54), sep='/n')