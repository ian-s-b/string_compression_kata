from typing import Union, List

import pytest

from string_compressor import StringCompressor


@pytest.mark.parametrize(
    ("str_to_compress", "expected_result"),
    [("aabcccaaa", "a2b1c3a3"), ("abc", "abc"), ("aaa", "a3"), ("kzzzi", "k1z3i1"), ("", ""), ("a", "a"),
     ("AAbcccAAA", "A2b1c3A3")])
def test_valid_compression(str_to_compress: str, expected_result: str) -> None:
    """
    Test used to check if the compression works as expected.

    :param str_to_compress: The string that will be compressed.
    :type str_to_compress: str
    :param expected_result: The expected compressed result.
    :type expected_result: str
    """
    compressed_string = StringCompressor.compress_str(str_to_compress)
    assert compressed_string == expected_result


@pytest.mark.parametrize("str_to_compress", [None, 1, ["Test"]])
def test_type_error(str_to_compress: Union[None, int, List[str]]) -> None:
    """
    Test if the compress method raises TypeError.

    :param str_to_compress: The string that will be compressed.
    :type str_to_compress: Union[None, int, List[str]]
    """
    with pytest.raises(TypeError):
        StringCompressor.compress_str(str_to_compress)


@pytest.mark.parametrize("str_to_compress", ["a2b1c3a3", "1", "2038232"])
def test_value_error(str_to_compress: str) -> None:
    """
    Test if the compress method raises ValueError.

    :param str_to_compress: The string that will be compressed.
    :type str_to_compress: str
    """
    with pytest.raises(ValueError):
        StringCompressor.compress_str(str_to_compress)


@pytest.mark.parametrize(
    ("str_to_compress", "expected_lower_result", "expected_result"),
    [("aabcccaaa", "a2b1c3a3", "a2b1c3a3"), ("AAbcccAAA", "a2b1c3a3", "A2b1c3A3"),
     ("AABCCCAAA", "a2b1c3a3", "A2B1C3A3")])
def test_case_sensitive_options(str_to_compress: str, expected_lower_result: str, expected_result: str) -> None:
    """
    Test if the case-sensitive options modifies the outputs as expected.

    :param str_to_compress: The string that will be compressed.
    :type str_to_compress: str
    :param expected_lower_result: The expected compressed lower result.
    :type expected_lower_result: str
    :param expected_result: The expected compressed result.
    :type expected_result: str
    """
    compressed_string_lower = StringCompressor.compress_str(str_to_compress, False)
    assert compressed_string_lower == expected_lower_result

    compressed_string = StringCompressor.compress_str(str_to_compress, True)
    assert compressed_string == expected_result
