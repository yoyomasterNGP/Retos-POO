class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start: "Point", end: "Point"):
        self.start = start
        self.end = end
    def compute_lenght(self)-> float:
        return ((self.end.x - self.start.x)**2 + (self.end.y - self.start.y)**2)**(0.5)
    def compute_slope(self)-> float:
        if self.end.x != self.start.x:
            slope = (self.end.y - self.start.y) / (self.end.x - self.start.x)
        else:
            slope = "infinity"
        return slope
    def compute_horizontal_cross(self)-> bool:
        return self.start.y * self.end.y >= 0
    def compute_vertical_cross(self)-> bool:
        return self.start.x * self.end.x >= 0
    def discretize_line(self, n: int):
        self.points_array = []
        if n <= 2: return self.start

        for i in range(n):
            div = i / (n-1)
            new_x = self.start.x + (self.end.x - self.start.x) * div
            new_y = self.start.y + (self.end.y - self.start.y) * div
            self.points_array.append(Point(new_x, new_y))

        return self.points_array

    
class Rectangle:
    def __init__(self, line1: "Line", line2: "Line", line3: "Line", line4: "Line"):
        self.lines = [line1, line2, line3, line4]
        self.w = line1.compute_lenght()
        self.h = line3.compute_lenght()
    def compute_area(self)-> float:
        return self.w * self.h
    


if __name__ == "__main__":
    inicio = Point(1, 1)
    final = Point(1, 2)
    linea = Line(inicio, final)
    print(linea.compute_lenght())
    print(linea.compute_slope())
    cruce_x = linea.compute_horizontal_cross
    if cruce_x:
        print("La línea si cruza por el eje x")
    else:
        print("La línea no cruza por el eje x")
    cruce_y = linea.compute_vertical_cross
    if cruce_y:
        print("La línea si cruza por el eje y")
    else:
        print("La línea no cruza por el eje y")
    discreto = (linea.discretize_line(3))
    print([(d.x, d.y) for d in discreto])

    inf_izq = Point(0, 0)
    inf_der = Point(3, 0)
    sup_der = Point(3, 5)
    sup_izq = Point(0, 5)
    arriba = Line(sup_der, sup_izq)
    izquierda = Line(sup_izq, inf_izq)
    abajo = Line(inf_izq, inf_der)
    derecha = Line(inf_der, sup_der)
    rectangulo = Rectangle(arriba, abajo, derecha, izquierda)
    print(rectangulo.compute_area())


"""   --- RETO 3 ---
Se definen todas las características de la línea a partir de un punto final y
un punto inicial, y se define una clase Rectangle compuesta por 4 líneas"""