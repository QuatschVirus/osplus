class IncorrectFormatException(BaseException):
    pass


def encode(txt: str) -> tuple:
    out = []
    for char in txt:
        n = ord(char)
        coded = [False, False, False, False, False, False, False, False]
        for i in range(0, 8):
            if n >= 2**i:
                coded[i] = True
                n -= 2**i
        out.append(coded)
    return tuple(out)


def decode(binlist: tuple) -> str:
    out = ""
    for char in binlist:
        if len(char) != 8:
            raise IncorrectFormatException(f"The inputted tuple ({binlist}) doesn't fit the 8bit scheme!")
        n = 0
        for i in range(0, 8):
            if binlist[i]:
                n += 2**i
        out += chr(n)
    return out


