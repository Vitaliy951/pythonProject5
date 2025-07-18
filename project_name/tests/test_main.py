import pytest
from project_name.src.main import Product, Category


@pytest.fixture(autouse=True)
def reset_category_product_counts():
    Category.category_count = 0  # Сбросить счетчик категорий перед каждым тестом


@pytest.fixture
def setup_products_and_categories():
    product1 = Product("Product 1", "Description 1", 10.0, 5)
    product2 = Product("Product 2", "Description 2", 15.0, 3)
    product3 = Product("Product 3", "Description 3", 20.0, 2)

    category1 = Category("Category 1", "Description A", [product1, product2])
    category2 = Category("Category 2", "Description B", [product3])

    return product1, product2, product3, category1, category2


def test_category_count(setup_products_and_categories):
    _, _, _, category1, category2 = setup_products_and_categories
    assert Category.get_category_count() == 2  # Ожидаем 2 категории


def test_product_count(setup_products_and_categories):
    _, _, _, category1, category2 = setup_products_and_categories
    assert category1.get_product_count() == 2  # Ожидаем 2 продукта в первой категории
    assert category2.get_product_count() == 1  # Ожидаем 1 продукт во второй категории
