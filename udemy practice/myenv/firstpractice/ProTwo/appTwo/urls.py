from django.conf.urls import url
from appTwo import views

urlpatterns = [
    url(r'records/', views.table, name='table'),
    url(r'form/', views.form, name='form')
]
