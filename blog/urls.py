from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
admin.autodiscover()

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^posts/', TemplateView.as_view(template_name='post.html')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
]