from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:slug>', views.DetailPostView.as_view(), name='detail_view'),
    re_path(r'(?P<month>[0-9]{2})/(?P<year>[0-9]{4})/$', views.MonthPostView.as_view(), name='month_view')
]
