from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import serializers
from rest_framework import status

from rest_framework import viewsets 


class HelloApiView(APIView):
    """First API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Get functions which gives API functions"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hi ingkstr!', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Create a hello world with our name"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = "Hello {}".format(name)
            return Response({'message': message})
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Testing PUT function"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Testing PATCH function"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Testing DELETE function"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    def list(self, request):
        """Return a hello message with GET function"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})