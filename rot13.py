from caesars_cipher import cesar_cifrar
from caesars_cipher import cesar_descifrar

text = "Im blue Da ba dee da ba di"

def rot13_cifrar(text):
    return cesar_cifrar(text, shift=13)

def rot13_descifrar(text):
    return cesar_descifrar(text, shift=13)

cifrado = rot13_cifrar(text)
decifrado = rot13_descifrar(cifrado)
print("Texto: "+ text)
print("Cifrado: " + cifrado)
print("Decifrado: " + decifrado)