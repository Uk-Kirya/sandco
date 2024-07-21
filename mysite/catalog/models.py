from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify


class Logos(models.Model):
    class Meta:
        verbose_name = "Логотип"
        verbose_name_plural = "Логотипы"

    image = models.FileField(upload_to='logos/')
    link = models.CharField(max_length=100, blank=True)


class Number(models.Model):
    class Meta:
        verbose_name = "Цифра"
        verbose_name_plural = "Статистика в цифрах"

    number = models.CharField(max_length=100, blank=True)
    text = models.CharField(max_length=100, blank=True)


class Benefit(models.Model):
    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"

    icon = models.FileField(upload_to='benefits/', blank=True)
    text = models.TextField(blank=True)


class Structure(models.Model):
    class Meta:
        verbose_name = "Состав"
        verbose_name_plural = "Состав песка"

    icon = models.FileField(upload_to='structure/', blank=True)
    title = models.CharField(max_length=100, blank=True)
    text = models.TextField(blank=True)


class Step(models.Model):
    class Meta:
        verbose_name = "Шаг"
        verbose_name_plural = "Как получается песок"

    image = models.FileField(upload_to='steps/', blank=True)
    text = models.TextField(blank=True)


class History(models.Model):
    class Meta:
        verbose_name = "Год"
        verbose_name_plural = "Хронология"

    year = models.IntegerField(blank=True)
    announcement = models.TextField(blank=True)
    text = RichTextUploadingField(blank=True)


class News(models.Model):
    class Meta:
        ordering = ['date']
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    date = models.CharField(max_length=100, blank=True, verbose_name='Дата публикации')
    title = models.CharField(max_length=100, blank=True, verbose_name='Заголовок')
    image = models.FileField(upload_to='news/', blank=True, verbose_name='Картинка')
    text = RichTextUploadingField(blank=True, verbose_name='Текст')
    is_published = models.BooleanField(default=True, verbose_name='Опубликована')
    slug = models.SlugField(max_length=100, blank=True, verbose_name='Slug')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)


class Category(models.Model):
    class Meta:
        verbose_name = 'Вид'
        verbose_name_plural = 'Виды'

    title = models.CharField(max_length=100, blank=True, verbose_name='Заголовок')
    image = models.FileField(upload_to='categories/', blank=True, verbose_name='Фотография')
    text = RichTextUploadingField(blank=True, verbose_name='Текст')
    order = models.IntegerField(max_length=100, blank=True, verbose_name='Порядковый номер', default=0)
    is_published = models.BooleanField(default=True, verbose_name='Опубликована')
    slug = models.SlugField(max_length=100, blank=True, verbose_name='Slug')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Advantage(models.Model):
    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'

    category = models.ForeignKey(Category, related_name='advantages', on_delete=models.CASCADE)
    image = models.FileField(upload_to='advantages/', blank=True, verbose_name='Иконка')
    text = models.CharField(max_length=150, blank=True, verbose_name='Текст')
    order = models.IntegerField(blank=True, default=0, verbose_name='Порядковый номер')


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    category = models.ManyToManyField(Category, related_name='products', verbose_name='Направления')
    title = models.CharField(max_length=100, blank=True, verbose_name='Заголовок')
    image = models.FileField(upload_to='products/', blank=True, verbose_name='Картинка')
    type = models.CharField(max_length=100, blank=True, verbose_name='Вид песка')
    fractions = RichTextUploadingField(blank=True, verbose_name='Фракции песка')
    text = RichTextUploadingField(blank=True, verbose_name='Текст')
    order = models.IntegerField(blank=True, default=0, verbose_name='Порядковый номер')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')
    slug = models.SlugField(max_length=100, blank=True, verbose_name='Slug')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Projects(models.Model):
    objects = None

    class Meta:
        ordering = ['date']
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    date = models.CharField(max_length=100, blank=True, verbose_name='Дата публикации')
    title = models.CharField(max_length=100, blank=True, verbose_name='Заголовок')
    announcement = models.TextField(blank=True, verbose_name='Краткое описание')
    image = models.FileField(upload_to='projects/', blank=True, verbose_name='Картинка')
    text = RichTextUploadingField(blank=True, verbose_name='Текст')
    category = models.ManyToManyField(Category, related_name='categories', verbose_name='Направления')
    product = models.ManyToManyField(Product, related_name='products_projects', verbose_name='Товары')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')
    slug = models.SlugField(max_length=100, blank=True, verbose_name='Slug')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Projects, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectPhoto(models.Model):
    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    project = models.ForeignKey(Projects, related_name='photos', on_delete=models.CASCADE)
    image = models.FileField(upload_to='projects/photos/', blank=True, verbose_name='Фото')


class ProductPhoto(models.Model):
    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    product = models.ForeignKey(Product, related_name='photos_product', on_delete=models.CASCADE)
    image = models.FileField(upload_to='products/photos/', blank=True, verbose_name='Фото')


class Spheres(models.Model):

    class Meta:
        verbose_name = 'Сфера'
        verbose_name_plural = 'Сферы применения'

    title = models.CharField(max_length=100, blank=True, verbose_name='Заголовок')
    image = models.FileField(upload_to='spheres/', blank=True, verbose_name='Картинка')
    link = models.CharField(max_length=100, blank=True, verbose_name='Ссылка на библиотеку')
    order = models.IntegerField(max_length=100, blank=True, default=0, verbose_name='Порядковый номер')


class Application(models.Model):

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Онлайн заявки с сайта'

    name = models.CharField(max_length=100, blank=True, verbose_name='Имя')
    phone = models.CharField(max_length=100, blank=True, verbose_name='Телефон')
    email = models.CharField(max_length=100, blank=True, verbose_name='Email')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата поступления')
    status = models.BooleanField(default=False, verbose_name='Обработана')


class ProductApplication(models.Model):

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы товаров'

    name = models.CharField(max_length=100, blank=True, verbose_name='Имя')
    phone = models.CharField(max_length=100, blank=True, verbose_name='Телефон')
    email = models.CharField(max_length=100, blank=True, verbose_name='Email')
    product = models.CharField(max_length=100, blank=True, verbose_name='Продукт')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата поступления')
    status = models.BooleanField(default=False, verbose_name='Обработан')