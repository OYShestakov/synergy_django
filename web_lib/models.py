from django.db import models
import uuid
from django.core import validators
from django.contrib.auth.models import User
from django.db.models import SET_NULL


class Author(models.Model):

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['id']
        unique_together = ('name', 'age')

    TYPES_LIT = (
        ('a', 'foreign'),
        ('b', 'domestic'),
        ('c', 'other')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(
        max_length=200,
        verbose_name='Имя автора',
        validators=[validators.RegexValidator(regex='^.*em$', message='Wrong')]
    )
    age = models.PositiveIntegerField(verbose_name='Возраст автора')
    email = models.EmailField(verbose_name='Почта автора')
    lit_type = models.CharField(max_length=200, verbose_name='Тип литературы', choices=TYPES_LIT, default='a')

    def info(self):
        name = ('Name: %s' % self.name)
        age = ('Age: %s' % self.age)
        lit_type = ('Type: %s' % self.lit_type)
        return [name, age, lit_type]

    def __str__(self):
        return self.name


class Book(models.Model):

    class Meta:
        get_latest_by = 'published'
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    title = models.CharField(max_length=200, verbose_name='Название книги')
    description = models.TextField()
    page_count = models.IntegerField()
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ExtUser(models.Model):

    desc = models.CharField(max_length=200, verbose_name='Описание пользователя')
    is_logged = models.BooleanField(verbose_name='Активность', default=True)
    user = models.OneToOneField(User, on_delete=SET_NULL, null=True)


class Product(models.Model):

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    name = models.CharField(max_length=200, verbose_name='Название товара')

class Store(models.Model):

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    name = models.CharField(max_length=200, verbose_name='Название магазина')
    products = models.ManyToManyField(Product, related_name='stores')