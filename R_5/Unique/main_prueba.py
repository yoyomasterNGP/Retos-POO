"""--- RETO 5: Único módulo para todas las figuras ---
En este reto, se hizo un único módulo para todo el código Shape.py.
Además, se probaron varios modos de importación, como:
- import Shape.Shape as Shape
- from Shape.Shape import *
- from Shape.Shape import Point, Line, Rectangle, Square, TriRectangle, Scalene, Isosceles, Equilateral
Debido a que hay varias clses, se decidió importar el módulo con un
alias para hacer un código más corto."""

"""
from Shape.Shape import (
    Point,
    Line,
    Rectangle,
    Square,
    TriRectangle,
    Scalene,
    Isosceles,
    Equilateral,
)

from Shape.Shape import *
"""

import Shape.Shape as Shape

Inicio = Shape.Point(0, 0)
Fin = Shape.Point(1, 1)
Linea = Shape.Line(Inicio, Fin)
# print(f"La longitud de la línea es de: {Linea.get_length()}")
punto_inf_izq = Shape.Point(0, 0)
rectangulo = Shape.Rectangle(punto_inf_izq, 5, 10)
cuadrado = Shape.Square(punto_inf_izq, 5)
triangulo_rec = Shape.TriRectangle(punto_inf_izq, 5, 10)
triangulo_esc = Shape.Scalene(Shape.Point(0, 0), Shape.Point(3, 2), Shape.Point(4, 6))
triangulo_iso = Shape.Isosceles(Shape.Point(0, 0), 5, 10)
triangulo_equ = Shape.Equilateral(Shape.Point(0, 0), 5)
print(f"Los vértices de la figura son: {triangulo_equ.get_vertices()}")
print(f"La longitud de los lados de la figura son: {triangulo_equ.get_edges()}")
print(f"Los ángulos internos de la figura son: {triangulo_equ.get_inner_angles()}")
print(f"El área de la figura es de {triangulo_equ.compute_area()} unidades cuadradas")
print(f"El perímetro de la figura es de {triangulo_equ.compute_perimeter()} unidades")
print(f"La figura es regular: {triangulo_equ.get_regular()}")
