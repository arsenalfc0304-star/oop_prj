from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count = len(self.__products)

    def add_product(self, product):
        if product not in self.__products:
            if isinstance(product, Product):
                self.__products.append(product)
            else:
                raise TypeError
            Category.product_count += 1

    @property
    def products(self):
        result = ""
        for product in self.__products:
            result += f"\n{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
        return result

    def __str__(self):
        products_sum = 0
        for product in self.__products:
            products_sum += product.quantity
        return f"{self.name}, количество продуктов: {products_sum} шт."

    def middle_price(self):
        try:
            return sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0
