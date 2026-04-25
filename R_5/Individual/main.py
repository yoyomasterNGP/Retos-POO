"""--- RETO 5: Módulos individuales ---
En este reto, se ha separado el código Shape.py en varios
módulos individuales para cada clase. Cada
clase se encuentra en un archivo separado, lo que hace que
sea más fácil de entender y modificar en el futuro."""

import Geometry as geometry

Inicio = geometry.Point(0, 0)
Fin = geometry.Point(1, 1)
Linea = geometry.Line(Inicio, Fin)
# print(f"La longitud de la línea es de: {Linea.get_length()}")
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
print(f"Los ángulos internos de la figura son: {triangulo_equ.get_inner_angles()}")
print(f"El área de la figura es de {triangulo_equ.compute_area()} unidades cuadradas")
print(f"El perímetro de la figura es de {triangulo_equ.compute_perimeter()} unidades")
print(f"La figura es regular: {triangulo_equ.get_regular()}")
