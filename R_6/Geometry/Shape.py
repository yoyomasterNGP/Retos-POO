import math


class Point:
    def __init__(self, x: float, y: float):
        # EXCEPCIÓN CASO 1: Validación de tipo de datos (TypeError)
        # Verifica que las coordenadas x e y sean estrictamente numéricas (int o float)
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError(
                "Las coordenadas del Punto (x, y) deben ser numéricas (int o float)."
            )

        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def set_x(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Las coordenadas x deben ser numéricas (int o float).")
        self.__x = value

    def get_y(self):
        return self.__y

    def set_y(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Las coordenadas y deben ser numéricas (int o float).")
        self.__y = value

    def compute_distance(self, other: "Point") -> float:
        return math.sqrt(
            (self.get_x() - other.get_x()) ** 2 + (self.get_y() - other.get_y()) ** 2
        )

    def __repr__(self):
        return f"({self.__x}, {self.__y})"


class Line:
    def __init__(self, start_point: Point, end_point: Point):
        if not isinstance(start_point, Point) or not isinstance(end_point, Point):
            raise TypeError("start_point y end_point deben ser instancias de Point.")
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
        if not self.__edges:
            return False
        primer_lado = self.__edges[0].get_length()

        for edge in self.__edges:
            if not math.isclose(edge.get_length(), primer_lado):
                self.__is_regular = False
                return self.__is_regular
        self.__is_regular = True
        return self.__is_regular


if __name__ == "__main__":
    try:
        Inicio = Point(0, 0)
        Fin = Point(1, 1)
        Linea = Line(Inicio, Fin)
        print(f"El punto de inicio es: {Inicio}")
        print(f"El punto de fin es: {Fin}")
        print(f"La longitud de la línea es de: {Linea.get_length()}")
    except (TypeError, ValueError) as e:
        print(f"Error inicializando puntos: {e}")
