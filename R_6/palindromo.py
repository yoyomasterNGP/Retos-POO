def es_palindromo(texto: str) -> bool:
    # Valida que el texto no esté vacío y que no contenga solo números
    if not texto.strip() or texto.strip().isdigit():
        raise ValueError(
            "El texto proporcionado no es una palabra válida. Revise que no esté vacío o que no contenga solo números."
        )

    texto = texto.lower()
    inicio: int = 0
    fin: int = len(texto) - 1
    while inicio < fin:
        if texto[inicio] != texto[fin]:
            return False
        inicio += 1
        fin -= 1
    return True


if __name__ == "__main__":
    try:
        palabra: str = str(input("Ingrese la palabra: "))
        if es_palindromo(palabra):
            print(f"'{palabra}' es palíndromo")
        else:
            print(f"'{palabra}' no es un palíndromo")
    except ValueError as e:
        print(e)
