from django.db.models import Count

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить объявление", 'url_name': 'add_page'},
    {'title': "Каталог", 'url_name': 'contact'}

]

class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('women'))

        context['menu'] = menu
        context['cats'] = cats

        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context

