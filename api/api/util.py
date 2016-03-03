def to_base(n, base):
    digs = "0123456789abcdefghijklmnopqrstuvwxyz"
    tmp = []
    while n:
        n, i = divmod(n, base)
        tmp.append(digs[i])
    return "".join(tmp[::-1])

def from_base(str, from_base, to_base):
    if to_base < 2 or to_base > 36 or from_base < 2 or from_base > 36:
        raise ValueError('Bases must be between 2 - 36')
    try:
        return to_base(int(str, from_base), to_base)
    except ValueError:
        try:
            n = int("".join([ch for ch in str if ch.isdigit()]), from_base)
            return to_base(n, to_base)
        except ValueError:
            return 0