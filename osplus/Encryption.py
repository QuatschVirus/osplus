def encode(key: str, txt: str):
    txt_c = ''
    for index in range(0, len(txt)):
        txt_int = ord(txt[index].lower()) + (ord(key[index % len(key)].upper()) - 65)
        if txt_int > 122:
            txt_int = txt_int - 26
        if txt_int < 97 or txt_int > 122:
            txt_c = txt_c + txt[index]
        else:
            txt_c = txt_c + chr(txt_int)
    return txt_c.upper()


def decode(key: str, txt_c: str):
    txt = ''
    for index in range(0, len(txt_c)):
        txt_int = ord(txt_c[index]) - (ord(key[index % len(key)].upper()) - 65)
        if txt_int < 97:
            txt_int = txt_int + 26
        if txt_int < 97 or txt_int > 122:
            txt = txt + txt_c[index]
        else:
            txt = txt + chr(txt_int)
    return txt
