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
    print("Ingrese números enteros. Ingrese 0 para finalizar.")
    while True:
        try:
            pri = int(input("Ingrese un entero o 0 para salir: "))
            if pri == 0:
                break
            lista.append(pri).
        # Valida que el valor ingresado sea un número entero (int)
        except ValueError as e:
            print(f"Entrada no válida. Por favor, ingrese un número entero. {e}")

    try:
        res: int = consecutivo(lista)
        print(f"La suma más grande de dos números consecutivos es: {res}")
    except IndexError as e:
        print(f"Error en el proceso, ingrese más de 2 números. {e}")
