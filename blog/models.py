from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField('заголовок', max_length=100)
    slug = models.SlugField('слаг')
    preambula = RichTextField('преамбула')
    text = RichTextField('текст')
    created = models.DateTimeField('создан', auto_now_add=True)

    created.editable = True

    def __str__(self):
        return f'Пост {self.id}'

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    text = RichTextField('текст')
    created = models.DateTimeField('создан', auto_now_add=True)

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self):
        return f'Комментарий {self.id}'
