from unbreakable_encryption import random_key, encrypt, decrypt
from faker import Faker
fake = Faker()



def test_random_key_is_random():
    random_key_1 = random_key(1)
    random_key_2 = random_key(1)
    assert random_key_1 != random_key_2



def test_encrypt_is_one_time():
    string = fake.word()
    encrypted_1 = encrypt(string)
    encrypted_2 = encrypt(string)
    assert encrypted_1 != encrypted_2

def test_encrypt_is_tuple():
    string = fake.word()
    encrypted = encrypt(string)
    assert type(encrypted) == tuple

def test_encryption():
    string = fake.bs()
    phrase_keys = encrypt(string)
    key1, key2 = phrase_keys
    result = decrypt(key1, key2)
    assert result == string








    

