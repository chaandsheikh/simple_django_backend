from rest_framework.views import APIView
from rest_framework.response import Response

class DemoAPIView(APIView):
    """ Demo api sample for APIview based class"""

    def get(self, request, format=None):
        return Response({'Demo': 'This is a demo for get method'})

