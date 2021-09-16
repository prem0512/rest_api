from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializer
from profiles_api import models
from profiles_api import permissions
# Create your views here.

class HelloApiView(APIView):
    """TEST API view"""

    serializer_class=serializer.HelloSerializer

    def get(self, request, format=None):
        """Resturns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as fuciton (get,post,patch,put,delete)',
            'is Similar to traditional Django View',
            'Gives you the mosr control over your applications logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello{name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of an object"""
        return Respone({'message': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete the object"""
        return Response({'Message': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API viewSet"""
    serializer_class=serializer.HelloSerializer

    def list(self, request):
        """return a hello message"""

        a_viewset = [
            'uses action(list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers'
            'provides more funcitonality with less code',
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})


    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an abj by id"""
        return Response({'http_mothod': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an obj"""
        return Response({'http_method':'UPDATE'})

    def partial_update(self, request, pk=None):
        """Handle Parital update"""
        return Response({'http_method':'PARTIAL_UPDATE'})

    def delete(self, request, pk=None):
        """Delete the object"""
        return Response({'http_method':'DELETE'})

class UserprofileViewSet(viewsets.ModelViewSet):
    """"handle creating and updating the profile"""
    serializer_class = serializer.UserProfileSerializer
    queryset = models.Userprofile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classess = (permissions.updateOwnProfile)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
