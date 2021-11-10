import py.test
from cipher_bm3019.cipher_bm3019 import cipher

def test_for_word():
    example = 'test'
    expected = 'uftu'
    actual = cipher(example, 1)
    assert actual == expected
        

