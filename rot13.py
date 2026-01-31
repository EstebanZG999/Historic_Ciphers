from caesars_cipher import cesar_cifrar
from caesars_cipher import cesar_decifrar

text = "Im blue Da ba dee da ba di"

def rot13_cifrar(text):
    return cesar_cifrar(text, shift=13)

def rot13_decifrar(text):
    return cesar_decifrar(text, shift=13)

cifrado = rot13_cifrar(text)
decifrado = rot13_decifrar(cifrado)
print("Texto: "+ text)
print("Cifrado: " + cifrado)
print("Decifrado: " + decifrado)