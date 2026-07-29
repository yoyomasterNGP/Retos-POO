def calc(a: float, b: float, op: str) -> float:
    match op:
        case "+":
            res: float = a + b
        case "-":
            res: float = a - b
        case "*":
            res: float = a * b
        case "/":
            res: float = a / b
    return res


if __name__ == "__main__":
    try:
        a = float(input("Ingrese el número a: "))
        b = float(input("Ingrese el número b: "))
        op = str(input("Ingrese el operador (+, -, *, /): "))
        sol = calc(a, b, op)
        print(f"El resultado de la operación {a} {op} {b} es {sol}")
    # Valida que el usuario ingrese un número válido, que sea tipo float
    # y que no se divida por cero
    except ValueError as e:
        print(f"Error de entrada: Asegúrate de ingresar números válidos. {e}")
    except ZeroDivisionError as e:
        print(f"No se puede dividir por cero. {e}")
