from django.conf.urls import include, url
from article import views

urlpatterns = [
    url(r'^$', views.articles, name='articles'),
    url(r'^add/?$', views.add_articles, name='add-articles'),
]