from typing import List

def compress_str(str_to_compress: str) -> str:
    previous_char: str = None
    str_count: int = 0
    compressed_chars: List[str] = []

    for char in str_to_compress:
        if previous_char is not None and char != previous_char:
            compressed_chars.append(previous_char + str(str_count))
            str_count = 1
        else:
            str_count += 1

        previous_char = char

    if previous_char is not None:
        compressed_chars.append(previous_char + str(str_count))

    compressed_str = str_to_compress
    if len(compressed_chars) <  len(str_to_compress):
        compressed_str =  ''.join(compressed_chars)
        
    return compressed_str
