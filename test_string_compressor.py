import pytest
from string_compressor import compress_str

@pytest.mark.parametrize(
        ("str_to_compress", "expected_compressed_string"),
        [("aabcccaaa", "a2b1c3a3"), ("abc", "abc"), ("aaa", "a3"), ("kzzzi", "k1z3i1"), ("", ""), ("a", "a"), ("AAbcccAAA", "A2b1c3A3")])
def test_valid_compression(str_to_compress, expected_compressed_string):
    compressed_string = compress_str(str_to_compress)
    assert compressed_string == expected_compressed_string

@pytest.mark.parametrize(("str_to_compress"), [None, 1, ["Test"]])
def test_type_error(str_to_compress):
    with pytest.raises(TypeError):
        compress_str(str_to_compress)

@pytest.mark.parametrize(("str_to_compress"), ["a2b1c3a3", "1", "2038232"])
def test_invalid_str(str_to_compress):
    with pytest.raises(ValueError):
        compress_str(str_to_compress)

@pytest.mark.parametrize(
        ("str_to_compress", "expected_compressed_string_lower", "expected_compressed_string"),
        [("aabcccaaa", "a2b1c3a3", "a2b1c3a3"), ("AAbcccAAA", "a2b1c3a3", "A2b1c3A3"), ("AABCCCAAA", "a2b1c3a3", "A2B1C3A3")])
def test_case_sensitive_options(str_to_compress, expected_compressed_string_lower, expected_compressed_string):
    compressed_string_lower = compress_str(str_to_compress, True)
    assert compressed_string_lower == expected_compressed_string_lower

    compressed_string = compress_str(str_to_compress, False)
    assert compressed_string == expected_compressed_string
