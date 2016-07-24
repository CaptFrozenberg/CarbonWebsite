from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import GaleryItem

def get_rows_count(obj_count):
    rows = divmod(obj_count, 4)
    if rows[1] == 0:
        rows = rows[0]
    else:
        rows = rows[0] + 1
    return rows

class GaleryView(TemplateView):
    template_name = 'photos.html'

    def get_context_data(self, **kwargs):
        context = super(GaleryView, self).get_context_data(**kwargs)
        items = GaleryItem.objects.all()
        # objects_count = len(items)
        # context['rows'] = get_rows_count(objects_count)
        # context['items_in_row'] = range(4)
        print(len(items))
        context['items'] = items
        return context