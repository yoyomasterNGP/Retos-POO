def calc(a: float, b: float, op: str) -> float:
    match op:
        case "+":
            res : float = a + b
        case "-":
            res : float = a - b
        case "*":
            res : float = a * b
        case "/":
            res : float = a / b
    return res

if __name__ == "__main__":
    a = float(input("Ingrese el número a: "))
    b = float(input("Ingrese el número b: "))
    op = str(input("Ingrese el operador: "))  
    sol = calc(a, b, op)
    print(f"El resultado de la operación {a} {op} {b} es {sol}")

"""   --- RETO 1 CALCULADORA ----
Se utiliza una función match-case para decidir que función se va 
a realizar y se devuelve el resultado"""