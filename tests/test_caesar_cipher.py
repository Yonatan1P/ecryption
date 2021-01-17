from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import encrypt, decrypt, crack

def test_encrypt():
    actual = encrypt("hello", 10)
    expected = "rovvy"
    assert actual == expected

def test_encrypt_capitals():
    actual = encrypt("Hello", 10)
    expected = "Rovvy"
    assert actual == expected

def test_encrypt_numbers():
    actual = encrypt("1234", 9)
    expected = "0123"
    assert actual == expected

def test_decrypt():
    encrypted_string = encrypt('hello', 10)
    actual = decrypt(encrypted_string, 10)
    expected = 'hello'
    assert actual == expected

def test_decrypt_capitals():
    encrypted_string = encrypt('Hello', 10)
    actual = decrypt(encrypted_string, 10)
    expected = 'Hello'
    assert actual == expected

def test_decrypt_numbers():
    encrypted_string = encrypt('1234', 5)
    actual = decrypt(encrypted_string, 5)
    expected = '1234'
    assert actual == expected

# def test_crack():
#     encrypted_string = encrypt('It was the best of times, it was the worst of times.', 9)
#     actual = crack(encrypted_string)
#     expected = 'It was the best of times, it was the worst of times.'
#     assert actual == expected

def test_version():
    assert __version__ == '0.1.0'
