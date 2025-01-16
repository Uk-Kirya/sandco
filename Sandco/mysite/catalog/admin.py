from django.contrib import admin
from .models import (
    Logos,
    Number,
    Benefit,
    Structure,
    Step,
    History,
    News,
    Projects,
    ProjectPhoto,
    Category,
    Advantage,
    Product,
    ProductPhoto,
    Application,
    Spheres,
    ProductApplication,
)
from django.utils.html import format_html
from django.http import HttpRequest
from django.conf import settings


class ProjectPhotoInline(admin.TabularInline):
    model = ProjectPhoto
    extra = 1


class CategoryAdvantageInline(admin.TabularInline):
    model = Advantage
    extra = 1


class ProductPhotoInline(admin.TabularInline):
    model = ProductPhoto
    extra = 1


@admin.action(description='Опубликовать')
def published(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset):
    queryset.update(is_published=True)


@admin.action(description='Снять с публикации')
def unpublished(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset):
    queryset.update(is_published=False)


@admin.register(Logos)
class LogosAdmin(admin.ModelAdmin):
    list_display = ('image_thumbnail', 'link')

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:100px;max-height:100px;" />', obj.image.url)
        return "No image"

    image_thumbnail.short_description = 'Логотип'


@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    list_display = ('get_number_verbose', 'get_text_verbose')

    def get_number_verbose(self, obj):
        return obj.number

    get_number_verbose.short_description = ("Цифра")

    def get_text_verbose(self, obj):
        return obj.text

    get_text_verbose.short_description = ("Текст")


@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('get_icon_verbose', 'get_text_verbose')

    def get_icon_verbose(self, obj):
        if obj.icon:
            return format_html('<img src="{}" style="max-width:100px;max-height:100px;" />', obj.icon.url)
        else:
            return "No icon"

    get_icon_verbose.short_description = ("Иконка")

    def get_text_verbose(self, obj):
        return obj.text

    get_text_verbose.short_description = ("Текст")


@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin):
    list_display = ('get_icon_verbose', 'get_title_verbose')

    def get_icon_verbose(self, obj):
        if obj.icon:
            return format_html('<img src="{}" width="64" height="64" />', obj.icon.url)
        else:
            return "No icon"

    get_icon_verbose.short_description = ("Иконка")

    def get_title_verbose(self, obj):
        return obj.title

    get_title_verbose.short_description = ("Заголовок")


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ('get_image_verbose', 'get_text_verbose')

    def get_image_verbose(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:100px;max-height:100px;" />', obj.image.url)
        else:
            return "No image"

    get_image_verbose.short_description = "Картинка"

    def get_text_verbose(self, obj):
        if len(obj.text) >= 100:
            return obj.text
        return obj.text[:100] + f'...'

    get_text_verbose.short_description = "Текст"


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('get_year_verbose', 'get_announcement_verbose')

    def get_year_verbose(self, obj):
        return obj.year

    get_year_verbose.short_description = "Год"

    def get_announcement_verbose(self, obj):
        if len(obj.text) >= 100:
            return obj.announcement[:100] + f'...'
        else:
            return obj.announcement

    get_announcement_verbose.short_description = "Краткий текст"


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    actions = [
        published,
        unpublished,
    ]
    list_display_links = ['get_image', 'get_title_verbose']
    list_display = ('get_image', 'get_title_verbose', 'date', 'is_published')
    prepopulated_fields = {'slug': ('title_for_url',)}
    ordering = '-date',

    def get_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:100px;max-height:100px;" />', obj.image.url)
        else:
            return "No image"

    get_image.short_description = "Картинка"

    def get_title_verbose(self, obj):
        if len(obj.title) >= 100:
            return obj.title[:100] + f'...'
        return obj.title

    get_title_verbose.short_description = "Заголовок"


@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    actions = [
        published,
        unpublished,
    ]
    inlines = [
        ProjectPhotoInline,
    ]
    list_display_links = [
        'get_image',
        'title'
    ]
    list_display = [
        'get_image',
        'title',
        'get_category_list',
        'get_products_list',
        'date',
        'is_published',
    ]
    prepopulated_fields = {
        'slug': (
            'title_for_url',
        )
    }
    ordering = '-date',

    def get_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:100px;max-height:100px;" />', obj.image.url)
        return "No image"

    get_image.short_description = "Картинка"

    def get_category_list(self, obj):
        return ', '.join([p.title for p in obj.category.all()])

    get_category_list.short_description = 'Направления'

    def get_products_list(self, obj: Projects):
        return ', '.join([p.title for p in obj.product.all()])

    get_products_list.short_description = 'Продукты'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'get_image',
        'title',
        'order',
        'is_published'
    )
    prepopulated_fields = {
        'slug': (
            'title_for_url',
        )
    }
    ordering = '-order',
    list_display_links = 'get_image', 'title'
    actions = [
        published,
        unpublished
    ]
    inlines = [
        CategoryAdvantageInline
    ]

    def get_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:100px;max-height:100px;" />', obj.image.url)
        else:
            return "No image"

    get_image.short_description = 'Фотография'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'get_image',
        'title',
        'get_category_list',
        'is_published',
    )
    search_fields = ['title', 'category__name']
    ordering = '-order',
    actions = [
        published,
        unpublished
    ]
    prepopulated_fields = {
        'slug': (
            'title_for_url',
        )
    }
    list_display_links = 'get_image', 'title'
    inlines = [
        ProductPhotoInline
    ]

    def get_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:100px;max-height:100px;" />', obj.image.url)
        else:
            return "No image"

    get_image.short_description = 'Картинка'

    def get_category_list(self, obj: Product) -> str:
        return ', '.join([category.title for category in obj.category.all()])

    get_category_list.short_description = 'Направления'


@admin.register(Spheres)
class SpheresAdmin(admin.ModelAdmin):
    list_display = (
        'get_image',
        'title',
        'order'
    )
    list_display_links = 'get_image', 'title'
    ordering = '-order',

    def get_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:100px;max-height:100px;" />', obj.image.url)
        else:
            return "No image"

    get_image.short_description = 'Картинка'


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone',
        'email',
        'category',
        'date',
        'status'
    )
    list_display_links = 'name',


@admin.register(ProductApplication)
class ProductApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone',
        'email',
        'product',
        'category',
        'date',
        'status'
    )
    list_display_links = 'name',
