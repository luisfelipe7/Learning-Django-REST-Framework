# Imports

# Don't need it anymore
# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import mixins
from rest_framework import generics
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action
# For user authentication
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
# Create your views here.

# request.POST  # Only handles form data.  Only works for 'POST' method.
# request.data  # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.

# return Response(data)  # Renders to content type as requested by the client.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Without ViewSet
#class SnippetList(generics.ListCreateAPIView):
#    queryset = Snippet.objects.all()
#    serializer_class = SnippetSerializer
#    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#    def get(self, request, *args, **kwargs):
#        return self.list(request, *args, **kwargs)
#    
#    def post(self, request, *args, **kwargs):
#        return self.create(request, *args, **kwargs)
#
#    # For user authentication
#    def perform_create(self, serializer):
#        serializer.save(owner=self.request.user)
#    #def pre_save(self, snip):
#   #    snip.owner = self.request.user
#    
#
#class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Snippet.objects.all()
#    serializer_class = SnippetSerializer
#    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                      IsOwnerOrReadOnly,)
#
#   def get(self, request, *args, **kwargs):
#        return self.retrieve(request, *args, **kwargs)
#
#    def put(self, request, *args, **kwargs):
#        return self.update(request, *args, **kwargs)
#    
#    def delete(self, request, *args, **kwargs):
#        return self.destroy(request, *args, **kwargs)



# For user authentication



class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)





#
# class UserList(generics.ListAPIView):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#
# Creating a single entry point to our API
#@api_view(['GET'])
#def api_root(request, format=None):
#    return Response({
#        'users': reverse('user-list', request=request, format=format),
#        'snippets': reverse('snippet-list', request=request, format=format)
#    })


# ******************** Other way to make the methods *******************
# @csrf_exempt
# Writing API Views
# class SnippetList(APIView):
#    """
#    List all snippets, or create a new snippet.
#    """
#    def get(self, format=None):
#        snippets= Snippet.objects.all()
#        serializer= SnippetSerializer(snippets, many=True)
#        return Response(serializer.data)
#
#    def post(self, request, format=None):
#        serializer= SnippetSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Other Version
# @api_view(['GET','POST'])
# def snippet_list(request, format=None):
#    """
#    List all code snippets, or create a new snippet.
#    """
#    if request.method == 'GET': # Request to send data
#        snippets = Snippet.objects.all()
#        serializer = SnippetSerializer(snippets, many=True)
#       return JsonResponse(serializer.data, safe=False)
#        return Response(serializer.data)
#
#    elif request.method == 'POST': # Request to receive data
#        data = JSONParser().parse(request)
#        serializer = SnippetSerializer(data=data)
#        if serializer.is_valid():
#           serializer.save()
# Old version
#           return JsonResponse(serializer.data, status=201)
#       return JsonResponse(serializer.errors, status=400)
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Other version
# @csrf_exempt
# writing API Views
# @api_view(['GET','PUT','DELETE'])
# def snippet_detail(request, pk, format=None):
# class SnippetDetail(APIView):
#    """
#     Retrieve, update or delete a code snippet.
#     """
# 
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#       return HttpResponse(status=404)
#       return Response(status=status.HTTP_404_NOT_FOUND)
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
# Old Version
#    if request.method == 'GET': # Get for pk
#        serializer = SnippetSerializer(snippet)
#       return JsonResponse(serializer.data)
#        return Response(serializer.data)
#    elif request.method == 'PUT': # Update a Snippet
#        data = JSONParser().parse(request)
#        serializer = SnippetSerializer(snippet, data=data)
#        if serializer.is_valid():
#            serializer.save()
#           return JsonResponse(serializer.data)
#       return JsonResponse(serializer.errors, status=400)
#            return Response(serializer.data)
#        return Response(status=status.HTTP_404_NOT_FOUND)
#    elif request.method == 'DELETE': # Delete a Snippet
#        snippet.delete()
#       return HttpResponse(status=204)
#       return Response(status=status.HTTP_204_NO_CONTENT)