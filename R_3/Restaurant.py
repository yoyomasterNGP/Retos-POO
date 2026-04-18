class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def calculate_total(self) -> float:
        return self.price


class Soup(MenuItem):
    def __init__(self, name: str, price: float, cream: bool = False):
        super().__init__(name, price)
        self.cream = cream


class Beef(MenuItem):
    def __init__(self, name: str, price: float, cooked: str):
        super().__init__(name, price)
        self.cooked = cooked


class Special(MenuItem):
    def __init__(self, name: str, price: float, vegan: bool = False):
        super().__init__(name, price)
        self.vegan = vegan


class Beverage(MenuItem):
    def __init__(self, name: str, price: float, alcohol: bool = False):
        super().__init__(name, price)
        self.alcohol = alcohol


class Dessert(MenuItem):
    def __init__(self, name: str, price: float, share: bool = False):
        super().__init__(name, price)
        self.share = share


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item: "MenuItem", portion: int):
        for _ in range(portion):
            self.items.append(item)

    def calculate_bill(self) -> float:
        subtotal = sum(item.calculate_total() for item in self.items)
        return subtotal

    def discount(self) -> float:
        total = self.calculate_bill()
        Special_discount = sum(1 for item in self.items if isinstance(item, Special))

        if Special_discount >= 2:
            print("--- Descuento del 20% aplicado (Promoción Platos Especiales) ---")
            return total * 0.8
        return total


if __name__ == "__main__":
    # Sopas
    sopa_tomate = Soup("Sopa de Maxi tomate", 50000)
    crema_espinaca = Soup("Crema de espinaca", 15000, cream=True)

    # Carnes
    baby_beef = Beef("Baby beef", 45000, "Bien asado")
    punta_anda = Beef("Punta de anca", 55000, "Tres cuartos")

    # Especiales
    wall_chicken = Special("Wall Chicken", 30000)
    chilly_dogs = Special("Chilly dogs", 25000)
    ensalada = Special("Ensalda de hierba verde y roja", 35000, vegan=True)

    # Bebidas
    jugo_wumpa = Beverage("Jugo de wumpa", 8000)
    hidromiel = Beverage("Hidromiel", 80000, alcohol=True)

    # Postre
    torta_chocolate = Dessert("Torta de chocolate", 20000, share=True)
    helado = Dessert("Helado de vainilla", 12000)

    pedido = Order()
    pedido.add_item(sopa_tomate, 5)
    pedido.add_item(wall_chicken, 2)
    pedido.add_item(jugo_wumpa, 1)
    pedido.add_item(helado, 1)

    print(f"Subtotal: ${pedido.calculate_bill()}")
    print(f"Total: ${pedido.discount()}")
