import math

from Geometry.Shape import Shape, Point, Line


class Triangle(Shape):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        vertices = [p1, p2, p3]
        edges = [Line(p1, p2), Line(p2, p3), Line(p3, p1)]
        super().__init__(vertices, edges)

    def compute_area(self):
        a, b, c = [edge.get_length() for edge in self.get_edges()]
        s: float = (a + b + c) / 2

        val = s * (s - a) * (s - b) * (s - c)
        if val < 0:
            raise ValueError("Los puntos proporcionados no forman un triángulo válido.")
        return math.sqrt(val)


class TriRectangle(Triangle):
    def __init__(self, p1: Point, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError(
                "Las dimensiones del Triángulo Rectángulo deben ser positivas y mayores a cero."
            )
        self.__width = width
        self.__height = height
        p2 = Point(p1.get_x() + width, p1.get_y())
        p3 = Point(p1.get_x(), p1.get_y() + height)
        super().__init__(p1, p2, p3)
        self.compute_inner_angles()

    def set_width(self, width: float):
        if width <= 0:
            raise ValueError(
                "El ancho del Triángulo Rectángulo debe ser positivo y mayor a cero."
            )
        self.__width = width
        p1 = self.get_vertices()[0]
        p2 = Point(p1.get_x() + self.__width, p1.get_y())
        p3 = Point(p1.get_x(), p1.get_y() + self.__height)
        new_vertices = [p1, p2, p3]
        new_edges = [Line(p1, p2), Line(p2, p3), Line(p3, p1)]
        self.set_vertices(new_vertices)
        self.set_edges(new_edges)
        self.compute_inner_angles()

    def set_height(self, height: float):
        if height <= 0:
            raise ValueError(
                "La altura del Triángulo Rectángulo debe ser positiva y mayor a cero."
            )
        self.__height = height
        p1 = self.get_vertices()[0]
        p2 = Point(p1.get_x() + self.__width, p1.get_y())
        p3 = Point(p1.get_x(), p1.get_y() + self.__height)
        new_vertices = [p1, p2, p3]
        new_edges = [Line(p1, p2), Line(p2, p3), Line(p3, p1)]
        self.set_vertices(new_vertices)
        self.set_edges(new_edges)
        self.compute_inner_angles()

    def compute_inner_angles(self):
        # EXCEPCIÓN CASO 3: Procedimiento matemático / División por cero (ZeroDivisionError)
        # Previene la división por cero al calcular los ángulos internos del triángulo rectángulo
        # arctan(height / width) si el ancho es cero
        if self.__width == 0:
            raise ZeroDivisionError(
                "No se pueden calcular los ángulos internos cuando el ancho es cero."
            )

        ang1 = 90
        ang2 = math.degrees(math.atan(self.__height / self.__width))
        ang3 = 180 - ang1 - ang2
        angles = [ang1, ang2, ang3]
        self.set_inner_angles(angles)


class Scalene(Triangle):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__(p1, p2, p3)
        self.compute_inner_angles()

    def set_p1(self, p1: Point):
        vertices = self.get_vertices()
        vertices[0] = p1
        self.set_vertices(vertices)
        edges = [
            Line(vertices[0], vertices[1]),
            Line(vertices[1], vertices[2]),
            Line(vertices[2], vertices[0]),
        ]
        self.set_edges(edges)
        self.compute_inner_angles()

    def set_p2(self, p2: Point):
        vertices = self.get_vertices()
        vertices[1] = p2
        self.set_vertices(vertices)
        edges = [
            Line(vertices[0], vertices[1]),
            Line(vertices[1], vertices[2]),
            Line(vertices[2], vertices[0]),
        ]
        self.set_edges(edges)
        self.compute_inner_angles()

    def set_p3(self, p3: Point):
        vertices = self.get_vertices()
        vertices[2] = p3
        self.set_vertices(vertices)
        edges = [
            Line(vertices[0], vertices[1]),
            Line(vertices[1], vertices[2]),
            Line(vertices[2], vertices[0]),
        ]
        self.set_edges(edges)
        self.compute_inner_angles()

    def compute_inner_angles(self):
        a, b, c = [edge.get_length() for edge in self.get_edges()]
        if 2 * a * c == 0 or 2 * a * b == 0:
            raise ZeroDivisionError(
                "La longitud de los lados no puede ser cero para el cálculo de ángulos internos."
            )
        ang1 = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        ang2 = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
        ang3 = 180 - ang1 - ang2
        angles = [ang1, ang2, ang3]
        self.set_inner_angles(angles)


class Isosceles(Triangle):
    def __init__(self, p1: Point, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError(
                "Las dimensiones del Triángulo Isósceles deben ser positivas y mayores a cero."
            )
        p2 = Point(p1.get_x() + width, p1.get_y())
        p3 = Point(p1.get_x() + width / 2, p1.get_y() + height)
        super().__init__(p1, p2, p3)
        self.compute_inner_angles()

    def compute_inner_angles(self):
        a, b, c = [edge.get_length() for edge in self.get_edges()]
        if 2 * a * c == 0:
            raise ZeroDivisionError(
                "La longitud de los lados no puede ser cero para el cálculo de ángulos internos."
            )
        ang1 = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        ang2 = ang1
        ang3 = 180 - ang1 - ang2
        angles = [ang1, ang2, ang3]
        self.set_inner_angles(angles)

    def set_width(self, width: float):
        if width <= 0:
            raise ValueError(
                "El ancho del Triángulo Isósceles debe ser positivo y mayor a cero."
            )
        p1 = self.get_vertices()[0]
        p2 = Point(p1.get_x() + width, p1.get_y())
        p3 = Point(
            p1.get_x() + width / 2, p1.get_y() + self.get_edges()[0].get_length()
        )
        new_vertices = [p1, p2, p3]
        new_edges = [Line(p1, p2), Line(p2, p3), Line(p3, p1)]
        self.set_vertices(new_vertices)
        self.set_edges(new_edges)
        self.compute_inner_angles()

    def set_height(self, height: float):
        if height <= 0:
            raise ValueError(
                "La altura del Triángulo Isósceles debe ser positiva y mayor a cero."
            )
        p1 = self.get_vertices()[0]
        p2 = Point(p1.get_x() + self.get_edges()[0].get_length(), p1.get_y())
        p3 = Point(
            p1.get_x() + self.get_edges()[0].get_length() / 2, p1.get_y() + height
        )
        new_vertices = [p1, p2, p3]
        new_edges = [Line(p1, p2), Line(p2, p3), Line(p3, p1)]
        self.set_vertices(new_vertices)
        self.set_edges(new_edges)
        self.compute_inner_angles()


class Equilateral(Triangle):
    def __init__(self, p1: Point, side: float):
        if side <= 0:
            raise ValueError(
                "La longitud del lado del Triángulo Equilátero debe ser positiva y mayor a cero."
            )
        p2 = Point(p1.get_x() + side, p1.get_y())
        p3 = Point(p1.get_x() + side / 2, p1.get_y() + (side * math.sqrt(3)) / 2)
        super().__init__(p1, p2, p3)
        self.set_inner_angles([60, 60, 60])

    def set_side(self, side: float):
        if side <= 0:
            raise ValueError(
                "La longitud del lado del Triángulo Equilátero debe ser positiva y mayor a cero."
            )
        p1 = self.get_vertices()[0]
        p2 = Point(p1.get_x() + side, p1.get_y())
        p3 = Point(p1.get_x() + side / 2, p1.get_y() + (side * math.sqrt(3)) / 2)
        new_vertices = [p1, p2, p3]
        new_edges = [Line(p1, p2), Line(p2, p3), Line(p3, p1)]
        self.set_vertices(new_vertices)
        self.set_edges(new_edges)


if __name__ == "__main__":
    try:
        punto_inf_izq = Point(0, 0)
        triangulo_rec = TriRectangle(punto_inf_izq, 5, 10)
        triangulo_esc = Scalene(Point(0, 0), Point(3, 2), Point(4, 6))
        triangulo_iso = Isosceles(Point(0, 0), 5, 10)
        triangulo_equ = Equilateral(Point(0, 0), 5)
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
    except (ValueError, TypeError, ZeroDivisionError) as e:
        print(f"Error en las operaciones del triángulo: {e}")
