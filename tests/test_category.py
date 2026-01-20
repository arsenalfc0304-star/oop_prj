def test_category_init(category_1):
    assert category_1.name == "Смартфоны"
    assert (
            category_1.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_1.category_count == 1
    assert category_1.product_count == 3

