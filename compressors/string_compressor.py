"""This module contains the StringCompressor class."""
from compressors.compression_strategies import CompressionStrategy, DefaultCompression
from compressors.validation_strategies import ValidationStrategy, DefaultValidation


class StringCompressor:
    """A class for compressing strings using customizable compression and validation strategies."""
    def __init__(self, compression_strategy: CompressionStrategy = DefaultCompression(),
                 validation_strategy: ValidationStrategy = DefaultValidation()):
        """

        :param compression_strategy: The compression strategy.
        :type compression_strategy: CompressionStrategy
        :param validation_strategy: The validation strategy.
        :type validation_strategy: ValidationStrategy
        """
        self._compression_strategy = compression_strategy
        self._validation_strategy = validation_strategy

    def compress_str(self, str_to_compress: str, is_case_sensitive: bool = True) -> str:
        """
        Check if the string can be compressed, then compress it.

        :param str_to_compress: The string to be compressed.
        :type str_to_compress: str
        :param is_case_sensitive: Lower output if not case-sensitive.
        :type is_case_sensitive: bool
        :return: The compressed string.
        :rtype: str
        """
        self._validation_strategy.validate_input(str_to_compress)

        if not is_case_sensitive:
            str_to_compress = str_to_compress.lower()

        return self._compression_strategy.compress(str_to_compress)
