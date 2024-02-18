"""This module defines validation strategies for the string to be compressed."""
import re
from abc import ABC, abstractmethod


class ValidationStrategy(ABC):
    """An abstract base class with validation methods for the string to be compressed."""
    @abstractmethod
    def validate_input(self, str_to_compress: str) -> None:
        """
        Method used to check if the string input valid by raising specific errors.

        :param str_to_compress: The string that will be compressed.
        :type str_to_compress: str
        """
        pass


class DefaultValidation(ValidationStrategy):
    """The default validation strategy for the string to be compressed."""
    def validate_input(self, str_to_compress: str) -> None:
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
