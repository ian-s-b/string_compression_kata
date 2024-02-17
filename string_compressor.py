import re
from typing import List, Optional


class StringCompressor:
    @staticmethod
    def _check_str_input(str_to_compress: str) -> None:
        """
        Method used to check if the string input valid.

        :param str_to_compress: The string that will be compressed.
        :type str_to_compress: str

        :raises TypeError: If the string to compress type is not correct.
        :raises ValueError: If the string to compress value contains number or empty spaces.
        """
        if not isinstance(str_to_compress, str):
            raise TypeError("The input to compress should be a string.")

        re_pattern = re.compile(r'[\d\s]')

        if re_pattern.search(str_to_compress):
            raise ValueError("The input to compress should not contain white spaces or numbers.")

    @classmethod
    def compress_str(cls, str_to_compress: str, is_case_sensitive: bool = True) -> str:
        """
        The compressed string method.

        :param str_to_compress: The string that will be compressed.
        :type str_to_compress: str
        :param is_case_sensitive: Lower output if not case-sensitive.
        :type is_case_sensitive: bool
        :return: The compressed string.
        :rtype: str
        """
        cls._check_str_input(str_to_compress)

        previous_char: Optional[str] = None
        str_count: int = 0
        compressed_chars: List[str] = []

        for char in str_to_compress:
            if not is_case_sensitive:
                char = char.lower()
            if previous_char is not None and char != previous_char:
                compressed_chars.append(previous_char + str(str_count))
                str_count = 1
            else:
                str_count += 1

            previous_char = char

        if previous_char is not None:
            compressed_chars.append(previous_char + str(str_count))

        if len(compressed_chars) < len(str_to_compress):
            return ''.join(compressed_chars)

        return str_to_compress
