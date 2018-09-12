from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    #     path('', api_root),
    # path('snippets/', snippet_list, name='snippet-list'),
    # path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    # path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    # path('users/', user_list, name='user-list'),
    # path('users/<int:pk>/', user_detail, name='user-detail')
]
#   url(r'^snippets/$', views.snippet_list),  # http://127.0.0.1:8000/snippets/
#   url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),  # http://127.0.0.1:8000/snippets/2

# We don't necessarily need to add these extra url patterns in, but it gives us a simple, clean way of referring to a specific format.


# We can control the format of the response that we get back, either by using the Accept header:
# http http://127.0.0.1:8000/snippets/ Accept:application/json  # Request JSON
# http http://127.0.0.1:8000/snippets/ Accept:text/html         # Request HTML

# Or by appending a format suffix:
# http http://127.0.0.1:8000/snippets.json  # JSON suffix
# http http://127.0.0.1:8000/snippets.api   # Browsable API suffix

# Similarly, we can control the format of the request that we send, using the Content-Type header.
# POST using form data
# http --form POST http://127.0.0.1:8000/snippets/ code="print 123"
#
#{
#  "id": 3,
#  "title": "",
#  "code": "print 123",
#  "linenos": false,
#  "language": "python",
#  "style": "friendly"
#}

# POST using JSON
# http --json POST http://127.0.0.1:8000/snippets/ code="print 456"
#
#{
#    "id": 4,
#    "title": "",
#    "code": "print 456",
#    "linenos": false,
#    "language": "python",
#    "style": "friendly"
#}