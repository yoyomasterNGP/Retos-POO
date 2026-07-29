"""--- RETO 6: Módulos individuales con manejo de excepciones ---"""

import Geometry as geometry

if __name__ == "__main__":
    try:
        Inicio = geometry.Point(0, 0)
        Fin = geometry.Point(1, 1)
        Linea = geometry.Line(Inicio, Fin)

        punto_inf_izq = geometry.Point(0, 0)
        rectangulo = geometry.Rectangle(punto_inf_izq, 5, 10)
        cuadrado = geometry.Square(punto_inf_izq, 5)
        triangulo_rec = geometry.TriRectangle(punto_inf_izq, 5, 10)
        triangulo_esc = geometry.Scalene(
            geometry.Point(0, 0), geometry.Point(3, 2), geometry.Point(4, 6)
        )
        triangulo_iso = geometry.Isosceles(geometry.Point(0, 0), 5, 10)
        triangulo_equ = geometry.Equilateral(geometry.Point(0, 0), 5)

        print(f"Los vértices de la figura son: {triangulo_equ.get_vertices()}")
        print(f"La longitud de los lados de la figura son: {triangulo_equ.get_edges()}")
        print(
            f"Los ángulos internos de la figura son: {triangulo_equ.get_inner_angles()}"
        )
        print(
            f"El área de la figura es de {triangulo_equ.compute_area()} unidades cuadradas"
        )
        print(
            f"El perímetro de la figura es de {triangulo_equ.compute_perimeter()} unidades"
        )
        print(f"La figura es regular: {triangulo_equ.get_regular()}")

    except TypeError as e:
        print(f"Error de tipo encontrado: {e}")
    except ValueError as e:
        print(f"Error de valor encontrado: {e}")
    except ZeroDivisionError as e:
        print(f"Error de cálculo (Division by zero): {e}")
    except Exception as e:
        print(f"Un error inesperado ocurrió: {e}")
