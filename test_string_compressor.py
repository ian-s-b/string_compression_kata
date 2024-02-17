from string_compressor import compress_str

def test_can_compress():
    compressed_string = compress_str("aabcccaaa")

    assert compressed_string == "a2b1c3a3"