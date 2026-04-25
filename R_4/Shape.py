"""--- RETO 4 ---
Se crea una superclase Shape compuesta de la clase Line y Point, todas con sus
respectivos atributos privados, de manera que se crean los respectivos setters
y getters. Además, se crean los métodos para calcular el área, el perímetro,
y para generar listas de los ángulos internos,vértices y lados; por último, se
crea un método para determinar si la figuraes regular o no.
Luego se crean las subclases Rectangle y Triangle que heredan de Shape, y a su vez,
estas se dividen en subclases, Square que hereda de Rectangle, TriRectangle,
Scalene, Isosceles y Equilateral que heredan de Triangle.
Se utiliza el polimorfismo para calcular el áreay los angulos internos de cada
figura, y se crean los métodos correspondientes para lograrlo."""

import math


class Point:
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def set_x(self, value: float):
        self.__x = value

    def get_y(self):
        return self.__y

    def set_y(self, value: float):
        self.__y = value

    def compute_distance(self, other: "Point") -> float:
        return math.sqrt(
            (self.get_x() - other.get_x()) ** 2 + (self.get_y() - other.get_y()) ** 2
        )

    def __repr__(self):
        return f"({self.__x}, {self.__y})"


class Line:
    def __init__(self, start_point: Point, end_point: Point):
        self.__start_point = start_point
        self.__end_point = end_point
        self.__length = start_point.compute_distance(end_point)

    def get_length(self):
        return self.__length

    def __repr__(self):
        return f"({self.__length})"


class Shape:
    def __init__(
        self, vertices: list[Point], edges: list[Line], is_regular: bool = False
    ):
        self.__vertices = vertices
        self.__edges = edges
        self.__inner_angles = []
        self.__is_regular = is_regular

    def get_vertices(self):
        return self.__vertices

    def set_vertices(self, vertices: list[Point]):
        self.__vertices = vertices

    def get_edges(self):
        return self.__edges

    def set_edges(self, edges: list[Line]):
        self.__edges = edges

    def compute_area(self):
        pass

    def compute_perimeter(self):
        return sum(edge.get_length() for edge in self.__edges)

    def compute_inner_angles(self):
        pass

    def set_inner_angles(self, angle: list):
        self.__inner_angles = angle

    def get_inner_angles(self):
        return self.__inner_angles

    def get_regular(self) -> bool:
        primer_lado = self.__edges[0].get_length()

        for edge in self.__edges:
            if not math.isclose(edge.get_length(), primer_lado):
                self.__is_regular = False
                return self.__is_regular
        self.__is_regular = True
        return self.__is_regular


class Rectangle(Shape):
    def __init__(self, bottom_left: Point, width: float, height: float):
        pbl = bottom_left
        pbr = Point(pbl.get_x() + width, pbl.get_y())
        ptr = Point(pbl.get_x() + width, pbl.get_y() + height)
        ptl = Point(pbl.get_x(), pbl.get_y() + height)

        vertices = [pbl, pbr, ptr, ptl]
        edges = [Line(pbl, pbr), Line(pbr, ptr), Line(ptr, ptl), Line(ptl, pbl)]

        super().__init__(vertices, edges)
        self.__width = width
        self.__height = height
        self.set_inner_angles([90, 90, 90, 90])

    def get_width(self) -> float:
        return self.__width

    def set_width(self, width: float):
        self.__width = width
        pbl = self.get_vertices()[0]
        x0 = pbl.get_x()
        y0 = pbl.get_y()
        pbr = Point(x0 + self.__width, y0)
        ptr = Point(x0 + self.__width, y0 + self.__height)
        ptl = Point(x0, y0 + self.__height)
        new_vertices = [pbl, pbr, ptr, ptl]
        new_edges = [Line(pbl, pbr), Line(pbr, ptr), Line(ptr, ptl), Line(ptl, pbl)]
        self.set_vertices(new_vertices)
        self.set_edges(new_edges)

    def set_height(self, height: float):
        self.__height = height
        pbl = self.get_vertices()[0]
        x0 = pbl.get_x()
        y0 = pbl.get_y()
        pbr = Point(x0 + self.__width, y0)
        ptr = Point(x0 + self.__width, y0 + self.__height)
        ptl = Point(x0, y0 + self.__height)
        new_vertices = [pbl, pbr, ptr, ptl]
        new_edges = [Line(pbl, pbr), Line(pbr, ptr), Line(ptr, ptl), Line(ptl, pbl)]
        self.set_vertices(new_vertices)
        self.set_edges(new_edges)

    def get_height(self):
        return self.__height

    def compute_area(self) -> float:
        return self.__width * self.__height


class Square(Rectangle):
    def __init__(self, bottom_left: Point, side: float):
        super().__init__(bottom_left, side, side)

    def set_side(self, side: float):
        self.set_width(side)
        self.set_height(side)


class Triangle(Shape):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        vertices = [p1, p2, p3]
        edges = [Line(p1, p2), Line(p2, p3), Line(p3, p1)]
        super().__init__(vertices, edges)

    def compute_area(self):
        a, b, c = [edge.get_length() for edge in self.get_edges()]
        s: float = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class TriRectangle(Triangle):
    def __init__(self, p1: Point, width: float, height: float):
        self.__width = width
        self.__height = height
        p2 = Point(p1.get_x() + width, p1.get_y())
        p3 = Point(p1.get_x(), p1.get_y() + height)
        super().__init__(p1, p2, p3)
        self.compute_inner_angles()

    def set_width(self, width: float):
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
        ang1 = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        ang2 = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
        ang3 = 180 - ang1 - ang2
        angles = [ang1, ang2, ang3]
        self.set_inner_angles(angles)


class Isosceles(Triangle):
    def __init__(self, p1: Point, width: float, height: float):
        p2 = Point(p1.get_x() + width, p1.get_y())
        p3 = Point(p1.get_x() + width / 2, p1.get_y() + height)
        super().__init__(p1, p2, p3)
        self.compute_inner_angles()

    def compute_inner_angles(self):
        a, b, c = [edge.get_length() for edge in self.get_edges()]
        ang1 = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        ang2 = ang1
        ang3 = 180 - ang1 - ang2
        angles = [ang1, ang2, ang3]
        self.set_inner_angles(angles)

    def set_width(self, width: float):
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
        p2 = Point(p1.get_x() + side, p1.get_y())
        p3 = Point(p1.get_x() + side / 2, p1.get_y() + (side * math.sqrt(3)) / 2)
        super().__init__(p1, p2, p3)
        self.set_inner_angles([60, 60, 60])

    def set_side(self, side: float):
        p1 = self.get_vertices()[0]
        p2 = Point(p1.get_x() + side, p1.get_y())
        p3 = Point(p1.get_x() + side / 2, p1.get_y() + (side * math.sqrt(3)) / 2)
        new_vertices = [p1, p2, p3]
        new_edges = [Line(p1, p2), Line(p2, p3), Line(p3, p1)]
        self.set_vertices(new_vertices)
        self.set_edges(new_edges)


if __name__ == "__main__":
    Inicio = Point(0, 0)
    Fin = Point(1, 1)
    Linea = Line(Inicio, Fin)
    # print(f"La longitud de la línea es de: {Linea.get_length()}")
    punto_inf_izq = Point(0, 0)
    rectangulo = Rectangle(punto_inf_izq, 5, 10)
    cuadrado = Square(punto_inf_izq, 5)
    triangulo_rec = TriRectangle(punto_inf_izq, 5, 10)
    triangulo_esc = Scalene(Point(0, 0), Point(3, 2), Point(4, 6))
    triangulo_iso = Isosceles(Point(0, 0), 5, 10)
    triangulo_equ = Equilateral(Point(0, 0), 5)
    print(f"Los vértices de la figura son: {triangulo_equ.get_vertices()}")
    print(f"La longitud de los lados de la figura son: {triangulo_equ.get_edges()}")
    print(f"Los ángulos internos de la figura son: {triangulo_equ.get_inner_angles()}")
    print(
        f"El área de la figura es de {triangulo_equ.compute_area()} unidades cuadradas"
    )
    print(
        f"El perímetro de la figura es de {triangulo_equ.compute_perimeter()} unidades"
    )
    print(f"La figura es regular: {triangulo_equ.get_regular()}")
