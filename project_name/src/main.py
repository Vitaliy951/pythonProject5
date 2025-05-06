class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    for product in [product1, product2, product3]:
        print(f"Название: {product.name}")
        print(f"Описание: {product.description}")
        print(f"Цена: {product.price}")
        print(f"Количество: {product.quantity}\n")

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(f"Описание категории: {category1.description}")
    print(f"Количество продуктов в категории: {len(category1.products)}")
    print(f"Общее количество категорий: {Category.category_count}")
    print(f"Общее количество продуктов: {Category.product_count}")

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(f"\nНазвание категории: {category2.name}")
    print(f"Описание категории: {category2.description}")
    print(f"Количество продуктов в категории: {len(category2.products)}")
    print(f"Продукты в категории: {[product.name for product in category2.products]}")

    print(f"Общее количество категорий: {Category.category_count}")
    print(f"Общее количество продуктов: {Category.product_count}")
