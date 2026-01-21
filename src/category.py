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
        self.products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        for product in self.__products:
            return f'{product.name}, {product.price} руб. Остаток: '


