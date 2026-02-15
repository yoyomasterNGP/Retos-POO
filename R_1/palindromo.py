def es_palindromo(texto: str) -> bool:
    texto = texto.lower()
    inicio : int = 0
    fin : int = len(texto) - 1
    while inicio < fin:
        if texto[inicio] != texto[fin]:
            return False
        inicio += 1
        fin -= 1
    return True

if __name__ == "__main__":
    palabra : str = str(input("Ingrese la palabra: "))
    if es_palindromo(palabra):
        print(f"'{palabra}' es palíndromo")
    else:
        print(f"'{palabra}' no es un palíndromo")

"""   --- RETO 1 PALINDROMO ---
Se compara la letra inicial de la palabra con la letra final
hasta que superen la 'mitad' de la palabra y se hayan revisado 
todas las letras. En caso de que no coincidan se devuelve False"""