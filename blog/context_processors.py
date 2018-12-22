from django.db.models import Count
from django.db.models.functions import Extract

from .models import Post


def monthes_list(*args, **kwargs):
    monthes_list = Post.objects.annotate(year=Extract('created', 'year'), month=Extract('created', 'month')). \
        values('year', 'month').annotate(count=Count('id'))
    return {'monthes_list': monthes_list}
