from modeltranslation.translator import register, TranslationOptions

from catalog.models import (
    Logos,
    Number,
    Benefit,
    Structure,
    Step,
    History,
    News,
    Category,
    Advantage,
    Product,
    Projects,
    ProjectPhoto,
    ProductPhoto,
    Spheres,
)


@register(Logos)
class LogosTranslationOptions(TranslationOptions):
    fields = ('image_alt', 'image_title')


@register(Number)
class NumberTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(Benefit)
class BenefitTranslationOptions(TranslationOptions):
    fields = ('icon_alt', 'icon_title', 'text')


@register(Structure)
class StructureTranslationOptions(TranslationOptions):
    fields = ('icon_alt', 'icon_title', 'title', 'text')


@register(Step)
class StepTranslationOptions(TranslationOptions):
    fields = ('image_alt', 'image_title', 'text')


@register(History)
class HistoryTranslationOptions(TranslationOptions):
    fields = ('year', 'announcement', 'text')


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('image_alt', 'image_title', 'title', 'date', 'text')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('image_alt', 'image_title', 'title', 'text')


@register(Advantage)
class AdvantageTranslationOptions(TranslationOptions):
    fields = ('image_alt', 'image_title', 'text')


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('image_alt', 'image_title', 'title', 'text', 'fractions', 'type')


@register(Projects)
class ProjectsTranslationOptions(TranslationOptions):
    fields = ('image_alt', 'image_title', 'title', 'text', 'date')


@register(ProjectPhoto)
class ProjectPhotoTranslationOptions(TranslationOptions):
    fields = ('image_alt', 'image_title')


@register(ProductPhoto)
class ProductPhotoTranslationOptions(TranslationOptions):
    fields = ('image_alt', 'image_title')


@register(Spheres)
class SpheresTranslationOptions(TranslationOptions):
    fields = ('image_alt', 'image_title', 'title')
