class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

def orientacion(p: "Point", q: "Point", r: "Point")-> int:
    ori: float = (q.x - p.x) * (r.y - q.y) - (q.y - p.y) * (r.x - q.x)
    if ori == 0: return 0
    return 1 if ori > 0 else 2

def se_cruzan(p1: "Point", p2: "Point", q1: "Point", q2: "Point")-> bool:
    o1 = orientacion(p1,q1,p2)
    o2 = orientacion(p1,q1,q2)
    o3 = orientacion(p2,q2,p1)
    o4 = orientacion(p2,q2,q1)
    if o1 != o2 and o3 != o4:
        return True
    else:
        return False

class Rectangle:
    def __init__(self, w: float, h: float, point: "Point", method: int):
        self.w = w
        self.h = h
        if method == 1:
            self.bl = point
            self.center = Point(self.bl.x + self.w/2, self.bl.y + self.h/2)
        elif method == 2:
            self.center = point
        elif method == 3:
            self.br = point
            self.opposite = Point(self.br.x - self.w, self.br.y + self.h)
            self.center = Point(self.br.x - self.w/2, self.br.y + self.h/2)

    def compute_area(self):
        return self.w * self.h
    def compute_perimeter(self):
        return (self.w * 2) + (self.h * 2)
    def compute_interference_point(self, interference: "Point")-> bool:
        return (self.center.x-self.w/2 <= interference.x <= self.center.x+self.w/2) and (self.center.y-self.h/2 <= interference.y <= self.center.y+self.h/2)
    def compute_interference_line(self, start: "Point", end: "Point"):
        left = self.center.x - self.w/2
        right = self.center.x + self.w/2
        bottom= self.center.y - self.h/2
        top = self.center.y + self.h/2
        p_bl = Point(left, bottom)
        p_br = Point(right, bottom)
        p_tl = Point(left, top)
        p_tr = Point(right, top)
        if se_cruzan(start, end, p_bl, p_br) or \
        se_cruzan(start, end, p_br, p_tr) or \
        se_cruzan(start, end, p_tr, p_tl) or \
        se_cruzan(start, end, p_tl, p_bl):
            return True
        else:
            return False
        
        

class Square(Rectangle):
    def __init__(self, s: float, point: "Point", method):
        super().__init__(w=s, h=s, point=point, method=method)


if __name__ == "__main__":
    punto_cuad = Point(0, 0)
    cuadrilatero = Rectangle(4, 2, punto_cuad, 1)
    punto = Point(1, 1)
    inicio = Point(0, 0)
    final = Point(0, 2)
    linea = Line(inicio, final)

    print(cuadrilatero.compute_area()) 
    print(cuadrilatero.compute_perimeter())
    dentro = cuadrilatero.compute_interference_point(punto)
    if dentro:
        print(f"El punto ({punto.x}, {punto.y}) está dentro del rectángulo")
    else:
        print(f"El punto ({punto.x}, {punto.y}) no está dentro del rectángulo")

    print(linea.compute_lenght)
    print(linea.compute_slope)
    eje_x = linea.compute_horizontal_cross
    if eje_x:
        print("La línea sí cruza el eje x")
    else:
        print("La línea no cruza el eje x")
    eje_y = linea.compute_vertical_cross
    if eje_y:
        print("La línea sí cruza el eje y")
    else: 
        print("La línea no cruza el eje y")

    linea_rec = cuadrilatero.compute_interference_line(inicio, final)
    if linea_rec:
        print(f"Al menos un parte de la línea está dentro del rectángulo")
    else:
        print(f"La línea no está dentro del rectángulo")
    




"""   --- RETO 3 ---
Primero definimos la clase punto, la cual utilizaremos a lo largo de todo
el código. La clase rectángulo, que toma como argumentos el ancho, la
altura y un punto, el cuál representa la esquina inferior izquierda, 
el centro o la esquina inferior derecho dependiendo del método que se 
elija, el cuál corresponde al último argumento; a partir de esto se
construye el rectángulo. Las funciones de aréa y perímetro se calculan 
utilizando las fórmulas básicas. Para verificar si un punto está dentro del
rectángulo verificamos que esté dentro del ancho y el alto del mismo. 
Finalmente para verificar si un segmento tiene parte dentro del rectángulo
o no se utiliza la orientación de puntos, el cuál se define en las funciones
orientación y se_cruza."""