abc = "abcdefghijklmnopqrstuvwxyz"

texto = "carros"

llave = "pelota"

def vigenere_cifrar(texto, llave):
    resultado = []
    llave = llave.lower()
    indice_clave = 0
    for c in texto:
        if c in abc:
            letra_clave = llave[indice_clave % len(llave)]
            salto = abc.index(letra_clave)
            idx = abc.index(c)
            new_indice = (idx + salto) % 26
            resultado.append(abc[new_indice])
            indice_clave += 1
        elif c == " ":
            resultado.append(" ")
        else:
            raise ValueError("No es letra minuscula")
        
    return ''.join(resultado)

def vigenere_decifrar(texto, llave):
    resultado = []
    llave = llave.lower()
    indice_clave = 0
    for c in texto:
        if c in abc:
            letra_clave = llave[indice_clave % len(llave)]
            salto = abc.index(letra_clave)
            idx = abc.index(c)
            new_indice = (idx - salto) % 26
            resultado.append(abc[new_indice])
            indice_clave += 1
        elif c == " ":
            resultado.append(" ")
        else:
            raise ValueError("No es letra minuscula")
        
    return ''.join(resultado)

print("Texto: " + texto)
cifrar = vigenere_cifrar(texto, llave)
decifrar = vigenere_decifrar(cifrar, llave)
print("Cifrado: " + cifrar)
print("Decifrado: " + decifrar)
