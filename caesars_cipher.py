abc = "abcdefghijklmnopqrstuvwxyz"
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

text = "Hola soy juan p"
shift = 3 

def cesar_cifrar(text, shift):
    resultado = []
    k = shift % 26
    for c in text:
        if c in abc:
            indice = abc.index(c)
            new_index = (indice + k) % 26
            resultado.append(abc[new_index])
        elif c in ABC:
            indice = ABC.index(c)
            new_index = (indice + k) % 26
            resultado.append(ABC[new_index])
        elif c == " ":
            resultado.append(" ")
        else:
            raise ValueError("Solo LETRAS")

    return ''.join(resultado)

def cesar_decifrar(text, shift):
    resultado = []
    k = shift % 26
    for c in text:
        if c in abc:
            indice = abc.index(c)
            new_index = (indice - k) % 26
            resultado.append(abc[new_index])
        elif c in ABC:
            indice = ABC.index(c)
            new_index = (indice - k) % 26
            resultado.append(ABC[new_index])
        elif c == " ":
            resultado.append(" ")
        else:
            raise ValueError("Solo LETRAS")

    return ''.join(resultado)

if __name__ == "__main__":
    print("Texto: "+ text)
    cifrado = cesar_cifrar(text, shift)
    print("Cifrado: " + cifrado)
    decifrado = cesar_decifrar(cifrado, shift)
    print("Decifrado: " + decifrado)