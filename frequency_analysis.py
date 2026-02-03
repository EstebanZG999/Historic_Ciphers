def analisis_frecuencia(texto):
    texto = texto.lower()
    conteo = {}
    for c in texto:
        if c.isprintable():
            if c in conteo:
                conteo[c] = conteo[c] + 1
            else:
                conteo[c] = 1
    tabla  = []
    total = sum(conteo.values())
    for (c, cantidad) in conteo.items():
        porcentaje = (cantidad / total) * 100
        tabla.append((c, cantidad, porcentaje))
    tabla = sorted(tabla, key= lambda x: x[1], reverse= True)
    return tabla

if __name__ == "__main__":
    texto = "Hola, yo soy Juan p, y esto es Jackass!!! 123"
    tabla = analisis_frecuencia(texto)
    for c, cantidad, porcentaje in tabla:
        print(f"{repr(c)} -> {cantidad} ({porcentaje:.2f}%)")