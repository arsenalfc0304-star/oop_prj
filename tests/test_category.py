def test_category_init_count(category_1, category_2):
    assert category_1.name == "Смартфоны"
    assert (
            category_1.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_2.category_count == 2


def test_category_product_count(category_1):
    assert category_1.product_count == 3

