def es_primo(num: int) -> bool:
    if num < 2:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

def lista_primo(lista_num: list) -> list:
    x : int = 0
    lista_final = []
    while x < len(lista_num):
        if es_primo(lista_num[x]) == True:
            lista_final.append(lista_num[x])
        x += 1
    return lista_final

if __name__ == "__main__":
    lista = []
    while True:
        pri = int(input("Ingrese un entero o 0 para salir: "))
        if pri == 0:
            break
        lista.append(pri)
    lista_real = lista_primo(lista)
    print(f"La lista de números primos es: {lista_real}")

"""   --- RETO NUMEROS PRIMOS ---
Primero se ejecuta una función para revisar si es un número primo;
después, se revisan todos los números de la lista y se crea una 
nueva lista únicamente con los números primos."""