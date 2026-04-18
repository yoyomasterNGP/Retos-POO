"""--- RETO 3 ---
Primero definimos la clase Point; y a partir de esta, definimos
la clase Line y Rectangle. La clase Line calcula la longitud, cruces
en los ejes y la pendiente de la línea a excepción de la pendiente
infinita, que se asigna como None. La clase Rectangle crea un rectángulo
a partir de varios métodos, por lo que se utiliza la función **kwargs
para leer los argumentos de la clase en función del método.
Las funciones de aréa y perímetro se calculan
utilizando las fórmulas básicas. Para verificar si un punto está dentro del
rectángulo verificamos que esté dentro del ancho y el alto del mismo.
Finalmente para verificar si un segmento tiene parte dentro del rectángulo
o no se utiliza la orientación de puntos, el cuál se define en las funciones
orientation y se_cruza."""


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


def orientation(p: Point, q: Point, r: Point) -> int:
    ori: float = (q.x - p.x) * (r.y - q.y) - (q.y - p.y) * (r.x - q.x)
    if ori == 0:
        return 0
    if ori > 0:
        return 1
    else:
        return 2


def se_cruzan(p1: "Point", p2: "Point", q1: "Point", q2: "Point") -> bool:
    o1 = orientation(p1, p2, q1)
    o2 = orientation(p1, p2, q2)
    o3 = orientation(q1, q2, p1)
    o4 = orientation(q1, q2, p2)
    if o1 != o2 and o3 != o4:
        return True
    else:
        return False


class Line:
    def __init__(self, start: "Point", end: "Point"):
        self.start = start
        self.end = end
        self.length = self.compute_lenght()
        self.slope = self.compute_slope()

    def compute_lenght(self) -> float:
        return (
            (self.end.x - self.start.x) ** 2 + (self.end.y - self.start.y) ** 2
        ) ** (0.5)

    def compute_slope(self):
        if self.end.x != self.start.x:
            slope = (self.end.y - self.start.y) / (self.end.x - self.start.x)
        else:
            slope = None
        return slope

    def compute_horizontal_cross(self) -> bool:
        return self.start.y * self.end.y <= 0

    def compute_vertical_cross(self) -> bool:
        return self.start.x * self.end.x <= 0

    def discretize_line(self, n: int):
        self.points_array = []
        if n <= 2:
            return self.start

        for i in range(n):
            div = i / (n - 1)
            new_x = self.start.x + (self.end.x - self.start.x) * div
            new_y = self.start.y + (self.end.y - self.start.y) * div
            self.points_array.append(Point(new_x, new_y))

        return self.points_array


class Rectangle:
    def __init__(self, method: int, **kwargs):
        if method == 1:
            bl: Point = kwargs["bl"]
            self.w: float = kwargs["w"]
            self.h: float = kwargs["h"]
            self.center = Point(bl.x + self.w / 2, bl.y + self.h / 2)

        elif method == 2:
            self.center: Point = kwargs["center"]
            self.w: float = kwargs["w"]
            self.h: float = kwargs["h"]

        elif method == 3:
            p1: Point = kwargs["p1"]
            p2: Point = kwargs["p2"]
            self.w = abs(p2.x - p1.x)
            self.h = abs(p2.y - p1.y)
            self.center = Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)

        elif method == 4:
            lines: list = kwargs["lines"]

            if len(lines) != 4:
                raise ValueError("Se necesitan exactamente 4 líneas.")

            for i in range(4):
                current_end = lines[i].end
                next_start = lines[(i + 1) % 4].start
                if current_end.x != next_start.x or current_end.y != next_start.y:
                    raise ValueError(f"La línea {i} no conecta con la línea {i + 1}.")

            for i in range(4):
                s1 = lines[i].slope
                s2 = lines[(i + 1) % 4].slope
                if s1 is None and s2 == 0:
                    continue
                if s2 is None and s1 == 0:
                    continue
                if s1 is None or s2 is None:
                    raise ValueError("Las líneas no forman ángulos de 90°.")
                if abs(s1 * s2 - (-1)) > 1e-9:
                    raise ValueError("Las líneas no forman ángulos de 90°.")

            points = [p for line in lines for p in (line.start, line.end)]
            xs = [p.x for p in points]
            ys = [p.y for p in points]

            self.w = max(xs) - min(xs)
            self.h = max(ys) - min(ys)
            self.center = Point((min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2)

        else:
            raise ValueError("El método debe ser 1, 2, 3 o 4.")

    def compute_area(self) -> float:
        return self.w * self.h

    def compute_perimeter(self) -> float:
        return 2 * (self.w + self.h)

    def compute_interference_point(self, point: Point) -> bool:
        return (
            self.center.x - self.w / 2 <= point.x <= self.center.x + self.w / 2
            and self.center.y - self.h / 2 <= point.y <= self.center.y + self.h / 2
        )

    def compute_interference_line(self, start: Point, end: Point) -> bool:

        left = self.center.x - self.w / 2
        right = self.center.x + self.w / 2
        bottom = self.center.y - self.h / 2
        top = self.center.y + self.h / 2

        p_bl = Point(left, bottom)
        p_br = Point(right, bottom)
        p_tr = Point(right, top)
        p_tl = Point(left, top)

        if self.compute_interference_point(start) or self.compute_interference_point(
            end
        ):
            return True

        return (
            se_cruzan(start, end, p_bl, p_br)  # lado inferior
            or se_cruzan(start, end, p_br, p_tr)  # lado derecho
            or se_cruzan(start, end, p_tr, p_tl)  # lado superior
            or se_cruzan(start, end, p_tl, p_bl)  # lado izquierdo
        )


class Square(Rectangle):
    def __init__(self, method: int, **kwargs):
        if method in (1, 2):
            s = kwargs.pop("s")
            super().__init__(method, w=s, h=s, **kwargs)
        else:
            super().__init__(method, **kwargs)


if __name__ == "__main__":
    # Rectángulo — método X
    inf_izq = Point(-5, -10)
    inf_der = Point(0, -10)
    sup_der = Point(0, 0)
    sup_izq = Point(-5, 0)
    arriba = Line(sup_der, sup_izq)
    izquierda = Line(sup_izq, inf_izq)
    abajo = Line(inf_izq, inf_der)
    derecha = Line(inf_der, sup_der)
    rect = Rectangle(method=4, lines=[arriba, izquierda, abajo, derecha])
    print("Área:", rect.compute_area())
    print("Perímetro:", rect.compute_perimeter())

    # Interferencia punto
    punto = Point(-1, -1)
    dentro = rect.compute_interference_point(punto)
    if dentro:
        print(f"El punto ({punto.x},{punto.y}) está dentro del rectángulo")
    else:
        print(f"El punto ({punto.x},{punto.y}) NO está dentro del rectángulo")

    # Línea
    inicio = Point(-1, -1)
    final = Point(2, 2)
    linea = Line(inicio, final)
    print(f"La longitud de la línea es {linea.compute_lenght()} unidades")
    print("La línea tiene una pendiente de:", linea.compute_slope())
    cruce_x = linea.compute_horizontal_cross()
    if cruce_x:
        print("La línea SI cruza por el eje x")
    else:
        print("La línea NO cruza por el eje x")
    cruce_y = linea.compute_vertical_cross()
    if cruce_y:
        print("La línea SI cruza por el eje y")
    else:
        print("La línea NO cruza por el eje y")
    discreto = linea.discretize_line(3)
    print([(d.x, d.y) for d in discreto])

    # Interferencia línea-rectángulo
    resultado = rect.compute_interference_line(inicio, final)
    if resultado:
        print("La línea SI interfiere con rectángulo")
    else:
        print("La línea NO interfiere con rectángulo")

    # Cuadrado — método X
    cuad = Square(method=2, center=Point(5, 5), s=3)
    print("\nCuadrado área:", cuad.compute_area())
    print("Cuadrado perímetro:", cuad.compute_perimeter())
