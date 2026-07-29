def es_anagrama(lista_palabras: list) -> list:
    # Verifica que la lista de palabras tenga al menos dos elementos para comparar
    if len(lista_palabras) < 2:
        raise IndexError(
            "Error: Se necesitan al menos 2 palabras en la lista para buscar anagramas."
        )

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
        try:
            pri: str = str(input("Ingrese una palabra o No para salir: "))
            if pri.lower() == "no":
                break
            if not pri.strip() or pri.strip().isdigit():
                raise ValueError(
                    "Error: La palabra no puede estar vacía o ser solo números."
                )
            lista.append(pri)
        except ValueError as e:
            print(e)

    try:
        res: list = es_anagrama(lista)
        if not res:
            print("No hay palabras anagramas dentro del arreglo")
        else:
            print(f"Las palabras anagramas son: {res}")
    except IndexError as e:
        print(e)
