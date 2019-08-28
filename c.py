# Fernet supports symmetric key cryptography 
from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)
print("Fernet key is {0}".format(key))
print("Cipher Suite is {0}".format(cipher_suite))
cipher_text = cipher_suite.encrypt(b"This is a secret message")
print("Cipher text is {0}".format(cipher_text))
plain_text = cipher_suite.decrypt(cipher_text)
print("Plain Text is {}".format(plain_text))

# Implementing MultiFernet (provides round key encryption)
from cryptography.fernet import Fernet, MultiFernet
key1 = Fernet(Fernet.generate_key())
key2 = Fernet(Fernet.generate_key())
print("Key 1 is {0} and Key 2 is {1}".format(key1,key2))
f = MultiFernet([key1,key2])
token = f.encrypt(b"Secret Message")
print("Token is {}".format(token))
print("Decrypted Text is {}".format(f.decrypt(token)))
