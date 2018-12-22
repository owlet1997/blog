from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage

from .models import Comment, Post


class CommentInlineAdmin(admin.StackedInline):
    model = Comment
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'user')
    prepopulated_fields = {'slug': ('title',)}
    inlines = (CommentInlineAdmin,)


admin.site.unregister(FlatPage)


class FlatPageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = FlatPage
        fields = '__all__'


@admin.register(FlatPage)
class FlatPageAdmin(admin.ModelAdmin):
    list_display = ('url', 'title')
    list_filter = ('registration_required', 'sites')
    form = FlatPageAdminForm
