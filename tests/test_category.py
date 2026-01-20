def test_category_init(category1, product1, product2, product3):
    assert category1.name == "Смартфоны"
    assert category1.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert category1.products == [product1, product2, product3]
    # assert category1.category_count == 5
    # assert category1.product_count == 5