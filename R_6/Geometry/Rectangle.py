from Geometry.Shape import Shape, Point, Line


class Rectangle(Shape):
    def __init__(self, bottom_left: Point, width: float, height: float):
        # EXCEPCIÓN CASO 2: Validación de valor (ValueError)
        # Verifica que el ancho y la altura sean estrictamente positivos y mayores que cero
        if width <= 0 or height <= 0:
            raise ValueError(
                "Las dimensiones del Rectángulo (Alto y ancho), deben ser positivas y mayores a cero."
            )

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
        if width <= 0:
            raise ValueError(
                "El ancho del Rectángulo debe ser positivo y mayor a cero."
            )
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
        if height <= 0:
            raise ValueError(
                "La altura del Rectángulo debe ser positiva y mayor a cero."
            )
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


if "__main__" == __name__:
    try:
        punto_inf_izq = Point(0, 0)
        rectangulo = Rectangle(punto_inf_izq, 5, 10)
        cuadrado = Square(punto_inf_izq, 5)
        print(f"Los vértices de la figura son: {rectangulo.get_vertices()}")
        print(f"La longitud de los lados de la figura son: {rectangulo.get_edges()}")
        print(f"Los ángulos internos de la figura son: {rectangulo.get_inner_angles()}")
        print(
            f"El área de la figura es de {rectangulo.compute_area()} unidades cuadradas"
        )
        print(
            f"El perímetro de la figura es de {rectangulo.compute_perimeter()} unidades"
        )
        print(f"La figura es regular: {rectangulo.get_regular()}")
    except (ValueError, TypeError) as e:
        print(f"Error creando el Rectángulo o Cuadrado: {e}")
