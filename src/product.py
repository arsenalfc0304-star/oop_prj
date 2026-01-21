class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_dict):
        return cls(name=product_dict['name'], description=product_dict['description'], price=product_dict['price'], quantity=product_dict['quantity'])
