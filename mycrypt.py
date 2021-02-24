import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
    for c in s:
        if c == "å" or c == "ä" or c == "ö":
            raise ValueError
            break
        elif c.isalpha():
            if c.islower():
                c=c.upper()
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
            crypted+=digitmapping[c]
        else:
            raise ValueError
            break

    return crypted

def decode(s):
    d = encode(s)
    if d.isalpha():
        if d.isupper():
            d=d.lower()
    return d