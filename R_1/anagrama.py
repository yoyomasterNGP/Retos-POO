def es_anagrama(lista_palabras: list) -> list:
    anagrama: list = set()
    i: int = 0
    x: int = 0
    while x < len(lista_palabras) - 1:
        for i in range(x + 1, len(lista_palabras)):
            if sorted(lista_palabras[x].lower()) == sorted(lista_palabras[i].lower()):
                anagrama.add(lista_palabras[x])
                anagrama.add(lista_palabras[i])
        x += 1
    return anagrama


if __name__ == "__main__":
    lista = []
    while True:
        pri: str = str(input("Ingrese una palabra o No para salir: "))
        if pri.lower() == "no":
            break
        lista.append(pri)
    res: list = es_anagrama(lista)
    if not res:
        print("No hay palabras anagramas dentro del arreglo")
    else:
        print(f"Las palabras anagramas son: {res}")

"""   --- RETO ANAGRAMAS ---
Se recibe la lista y se empiezan a comparar las palabras desde el punto
de partida en adelante, de esta manera no se comparan las mismas palabras
dos veces. Además, se utilizo el set() para eliminar las palabras repetidas"""
