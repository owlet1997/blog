from datetime import datetime

from django.contrib import messages
from django.contrib.messages import ERROR
from django.db.models.functions import Extract
from django.views.generic import ListView
from django.views.generic.edit import UpdateView

from .models import Post


class IndexView(ListView):
    template_name = 'index.html'
    model = Post
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flatpage'] = {'url': '/'}
        return context


class DetailPostView(UpdateView):
    template_name = 'post.html'
    model = Post
    slug_field = 'slug'
    fields = ['text']
    form_class = None

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        comment_text = request.POST.get('comment_text')
        if comment_text and request.user:
            self.object.comments.create(user=request.user, text=comment_text)
        else:
            messages.add_message(request, ERROR, 'Комментарий пустой или неавторизованный пользователь')
        return self.render_to_response(context=context)


class MonthPostView(ListView):
    template_name = 'index.html'
    model = Post

    def get(self, request, *args, **kwargs):
        month = int(kwargs.get('month', datetime.now().month))
        year = int(kwargs.get('year', datetime.now().year))
        self.object_list = self.get_queryset()
        self.object_list = self.object_list.annotate(year=Extract('created', 'year'),
                                                     month=Extract('created', 'month')). \
            filter(month=month, year=year).order_by('created')
        context = self.get_context_data()
        return self.render_to_response(context)
