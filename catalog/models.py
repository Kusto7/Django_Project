from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название категории')
    description = models.CharField(max_length=150, verbose_name='Описание категории')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Категории'  # Настройка для наименования набора объектов


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название продукта')
    description = models.CharField(max_length=150, verbose_name='Описание продукта')
    image = models.ImageField(upload_to='product_media/', verbose_name='Превью продукта', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.IntegerField(default=0, verbose_name='Цена за покупку')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    date_modified = models.DateField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Продукты'  # Настройка для наименования набора объектов
