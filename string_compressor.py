from typing import List

def compress_str(str_to_compress: str) -> str:
    previous_char: str = None
    str_count: int = 0
    compressed_str: List[str] = []

    for char in str_to_compress:
        if previous_char is not None and char != previous_char:
            compressed_str.append(previous_char + str(str_count))
            str_count = 1
        else:
            str_count += 1

        previous_char = char

    if previous_char is not None:
        compressed_str.append(previous_char + str(str_count))

    return ''.join(compressed_str)
