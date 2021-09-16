from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """TEST API view"""

    def get(self, request, format=None):
        """Resturns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as fuciton (get,post,patch,put,delete)',
            'is Similar to traditional Django View',
            'Gives you the mosr control over your applications logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview':an_apiview})
