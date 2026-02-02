BASE62_ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE = 62

def encode_base62(num: int) -> str:
    if num == 0:
        return BASE62_ALPHABET[0]

    chars = []
    while num > 0:
        remainder = num % BASE
        chars.append(BASE62_ALPHABET[remainder])
        num //= BASE

    return ''.join(reversed(chars))

print(encode_base62(125))   # cb
print(encode_base62(1234567))


class IdGenerator:
    def __init__(self, start=1):
        self.current = start

    def next_id(self) -> int:
        id_ = self.current
        self.current += 1
        return id_

id_gen = IdGenerator()

def shorten_url(long_url: str) -> str:
    # id_ = id_gen.next_id()
    id_ = 178217821389123
    short_code = encode_base62(id_)
    print(f"ID: {id_} short_code: {short_code}")
    # store: (short_code -> long_url)
    return short_code


# Demo
# print(shorten_url("https://example.com"))  # 1 → "1"
# print(shorten_url("https://google.com"))   # 2 → "2"
# print(shorten_url("https://openai.com"))   # 3 → "3"
print(shorten_url("https://example.com")) # OBCJinh9