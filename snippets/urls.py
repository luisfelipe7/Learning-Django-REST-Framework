from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),  # http://127.0.0.1:8000/snippets/
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),  # http://127.0.0.1:8000/snippets/2
]