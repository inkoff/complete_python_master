class Product:
    """ghbdtn"""

    def __init__(self, price: int) -> None:
        self.price = price

    @property
    def price(self) -> int:
        """price property"""
        return self.__price

    @price.setter
    def price(self, value: int) -> int:
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


product = Product(78)

print(product.price)
print(type(product.price))
