from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        category_list = [
            {'id': 1, 'category_name': 'Фрукты', 'category_description': 'Фрукты из Кавказа'},
            {'id': 2, 'category_name': 'Овощи', 'category_description': 'Овощи прям с огорода'}
        ]

        categories_for_create = []
        for category in category_list:
            categories_for_create.append(Category(**category))

        print(categories_for_create)

        Category.objects.bulk_create(categories_for_create)

        products_list = [
            {'product_name': 'Картошка', 'product_description': 'Картоха из Беларуссии',
             'product_category': Category.objects.get(pk=2), 'product_price': 100},

            {'product_name': 'Огурец', 'product_description': 'Огурцы хрустящие',
             'product_category': Category.objects.get(pk=2), 'product_price': 45},

            {'product_name': 'Помидор', 'product_description': 'Самые спелые, красные помидоры',
             'product_category': Category.objects.get(pk=2), 'product_price': 45},

            {'product_name': 'Банан', 'product_description': 'Бананы из Африки',
             'product_category': Category.objects.get(pk=1), 'product_price': 120},

            {'product_name': 'Кокос', 'product_description': 'Только кокосы с высоких пальм',
             'product_category': Category.objects.get(pk=1), 'product_price': 155},

            {'product_name': 'Яблоко', 'product_description': 'Яблочки от бабули',
             'product_category': Category.objects.get(pk=1), 'product_price': 99}
        ]

        products_for_create = []
        for product in products_list:
            products_for_create.append(Product(**product))

        print(products_for_create)

        Product.objects.bulk_create(products_for_create)
