import pytest
from string_compressor import compress_str

@pytest.mark.parametrize(
        ("str_to_compress", "expected_compressed_string"),
        [("aabcccaaa", "a2b1c3a3"), ("abc", "a1b1c1"), ("aaa", "a3"), ("kzzzi", "k1z3i1"), ("", "")])
def test_compress_str(str_to_compress, expected_compressed_string):
    compressed_string = compress_str(str_to_compress)
    assert compressed_string == expected_compressed_string
