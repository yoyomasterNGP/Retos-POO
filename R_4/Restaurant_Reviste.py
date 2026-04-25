"""--- RETO 4: Restaurante Reviste ---
En este reto, se ha añadido al código del restaurante hecho
previamente atributos privados a las clases, así como métodos
getter y setter para cada uno de ellos. También se introdujo
la clase "MedioPago" con sus respectivas subclases "Tarjeta"
y "Efectivo" para manejar diferentes formas de pago."""


class MenuItem:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def set_name(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_price(self, price: float):
        self.__price = price

    def get_price(self) -> float:
        return self.__price

    def calculate_total(self) -> float:
        return self.__price


class Soup(MenuItem):
    def __init__(self, name: str, price: float, cream: bool = False):
        super().__init__(name, price)
        self.__cream = cream

    def set_cream(self, cream: bool):
        self.__cream = cream

    def get_cream(self):
        return self.__cream


class Beef(MenuItem):
    def __init__(self, name: str, price: float, cooked: str):
        super().__init__(name, price)
        self.__cooked = cooked

    def set_cooked(self, cooked: str):
        self.__cooked = cooked

    def get_cooked(self):
        return self.__cooked


class Special(MenuItem):
    def __init__(self, name: str, price: float, vegan: bool = False):
        super().__init__(name, price)
        self.__vegan = vegan

    def set_vegan(self, vegan: bool):
        self.__vegan = vegan

    def get_vegan(self):
        return self.__vegan


class Beverage(MenuItem):
    def __init__(self, name: str, price: float, alcohol: bool = False):
        super().__init__(name, price)
        self.__alcohol = alcohol

    def set_alcohol(self, alcohol: bool):
        self.__alcohol = alcohol

    def get_alcohol(self):
        return self.__alcohol

    def calculate_total(self) -> float:
        if self.get_alcohol():
            return self.get_price() * 1.15
        else:
            return self.get_price()


class Dessert(MenuItem):
    def __init__(self, name: str, price: float, share: bool = False):
        super().__init__(name, price)
        self.__share = share

    def set_share(self, share: bool):
        self.__share = share

    def get_share(self):
        return self.__share


class Order:
    def __init__(self):
        self.__items = []

    def add_item(self, item: "MenuItem", portion: int):
        for _ in range(portion):
            self.__items.append(item)

    def calculate_bill(self) -> float:
        subtotal = sum(item.calculate_total() for item in self.__items)
        return subtotal

    def discount(self) -> float:
        total = self.calculate_bill()
        Special_discount = sum(1 for item in self.__items if isinstance(item, Special))

        if Special_discount >= 2:
            print("--- Descuento del 20% aplicado (Promoción Platos Especiales) ---")
            return total * 0.8
        return total

    def process_payment(self, payment_method: "MedioPago"):
        pay = self.discount()
        print(f"Total a pagar: ${pay}")
        payment_method.pagar(pay)


class MedioPago:
    def __init__(self):
        pass

    def pagar(self, pay):
        raise NotImplementedError("Subclases deben implementar pagar()")


class Tarjeta(MedioPago):
    def __init__(self, numero: str, cvv: int):
        super().__init__()
        self.numero = numero
        self.cvv = cvv

    def pagar(self, pay):
        print(f"Pagando {pay} con tarjeta {self.numero[-4:]}")


class Efectivo(MedioPago):
    def __init__(self, monto_entregado):
        super().__init__()
        self.monto_entregado = monto_entregado

    def pagar(self, pay):
        if self.monto_entregado >= pay:
            print(f"Pago realizado en efectivo. Cambio: {self.monto_entregado - pay}")
        else:
            print(
                f"Fondos insuficientes. Faltan {pay - self.monto_entregado} para completar el pago."
            )


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
    pedido.add_item(crema_espinaca, 2)
    pedido.add_item(ensalada, 1)
    pedido.add_item(hidromiel, 1)
    pedido.add_item(helado, 1)

    print("--- Procesando pago ---")
    pago = Tarjeta("1111222233334444", 123)
    pedido.process_payment(pago)
