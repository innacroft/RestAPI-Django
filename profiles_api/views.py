from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
  """Test API View"""
  def get(self, request, format=None):
    """Returns a list of APIView features"""
    an_apiview=[
      'Uses HTTP methods as function (get, post, patch, put, delete)',
      'Is similar to traditional Django view',
      'Gives you the most control over you application logic',
      'is mapped manually to URLs',
    ]
    return Response({'message':'hello','an_appiview':an_apiview})
