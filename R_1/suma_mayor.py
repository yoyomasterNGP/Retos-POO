def consecutivo(lista_num: list) -> list:
    mayor: int = lista_num[0] + lista_num[1]
    i: int = 2
    while i <= len(lista_num) - 1:
        suma: int = lista_num[i - 1] + lista_num[i]
        if suma > mayor:
            mayor = suma
        i += 1
    return mayor


if __name__ == "__main__":
    lista = []
    while True:
        pri = int(input("Ingrese un entero o 0 para salir: "))
        if pri == 0:
            break
        lista.append(pri)
    res: int = consecutivo(lista)
    print(f"La suma más grande de dos números consecutivos en la lista es: {res}")

"""   --- RETO SUMA No. CONSECUTIVOS
Se establece la suma de los dos primeros números del arreglo, 
a partir de ahí se recorre toda la lista y se van comparando
con la suma inicial. Cuando hay una suma mayor se establece
un nuevo número hasta que se haya recorrido toda la lista."""
