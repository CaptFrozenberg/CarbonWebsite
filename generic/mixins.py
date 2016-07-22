from django.views.generic.base import ContextMixin
from django.conf import settings

class LangListMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(LangListMixin, self).get_context_data(**kwargs)
        context['LANGUAGES'] = settings.LANGUAGES
        return context
