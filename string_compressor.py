import re
from typing import List


def _chek_str_input(str_to_compress: str) -> None:
    if not isinstance(str_to_compress, str):
        raise TypeError("The input to compress should be a string.")

    re_pattern = re.compile(r'[\d\s]')

    if re_pattern.search(str_to_compress):
        raise ValueError("The input to compress should not contain white spaces or numbers.")


def compress_str(str_to_compress: str, lower_compression: bool = False) -> str:
    _chek_str_input(str_to_compress)

    previous_char: str = None
    str_count: int = 0
    compressed_chars: List[str] = []

    for char in str_to_compress:
        if lower_compression:
            char = char.lower()
        if previous_char is not None and char != previous_char:
            compressed_chars.append(previous_char + str(str_count))
            str_count = 1
        else:
            str_count += 1

        previous_char = char

    if previous_char is not None:
        compressed_chars.append(previous_char + str(str_count))

    if len(compressed_chars) <  len(str_to_compress):
        return ''.join(compressed_chars)

    return str_to_compress
