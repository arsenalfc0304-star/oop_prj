import pytest

from src.product import Product


def test_product_init(product_1):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_new_product(capsys):
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5
    assert capsys.readouterr().out == 'Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)\n'

def test_product_price_setter(product_1):
    assert product_1.price == 180000.0
    product_1.price = 230000.0
    assert product_1.price == 230000.0
    product_1.price = -180000.0
    assert product_1.price == 230000.0


def test_product_str(product_1):
    assert str(product_1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product_1, product_2):
    assert product_1 + product_2 == 2580000.0


def test_product_add_incorrect(product_7, product_8):
    with pytest.raises(TypeError):
        product_7 + product_8
