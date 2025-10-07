from modeltranslation.translator import register, TranslationOptions,register
from .models import News,Category

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields=( 'title','body')

@register(Category)
class CategorytranslationOptions(TranslationOptions):
    fields=('name',)