"""This module defines string compression strategies."""
from abc import ABC, abstractmethod
from typing import Optional, List


class CompressionStrategy(ABC):
    """An abstract base class with methods used for string compression"""
    @abstractmethod
    def compress(self, str_to_compress) -> str:
        """
        Compresses the requested string.

        :param str_to_compress: The string to be compressed.
        :type str_to_compress: str
        :return: The compressed string.
        :rtype: str
        """


class DefaultCompression(CompressionStrategy):
    """The default string compression strategy."""
    def compress(self, str_to_compress: str) -> str:
        """
        Compresses the requested string.

        :param str_to_compress: The string to be compressed.
        :type str_to_compress: str
        :return: The compressed string.
        :rtype: str
        """
        if str_to_compress == "abceee":
            a=1

        previous_char: Optional[str] = None
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

        if len(compressed_chars)*2 < len(str_to_compress):
            return ''.join(compressed_chars)

        return str_to_compress
