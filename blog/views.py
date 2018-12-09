from django.db.models.functions import ExtractYear, Extract
from django.views.generic import TemplateView, ListView
from .models import Post


class IndexView(ListView):
    template_name = 'index.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['monthes_list'] = Post.objects.\
            annotate(year=Extract('created', 'year'), month=Extract('created', 'month')).values('year', 'month').\
            distinct()
        return context
