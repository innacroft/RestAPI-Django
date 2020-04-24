from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken #login
from rest_framework.settings import api_settings #login

from profiles_api import serializer
from profiles_api import models
from profiles_api import permissions
# Create your views here.
class HelloApiView(APIView):

  """Test API View"""
  serializer_class= serializer.HelloSerializer
  def get(self, request, format=None):
    """Returns a list of APIView features"""
    an_apiview=[
      'Uses HTTP methods as function (get, post, patch, put, delete)',
      'Is similar to traditional Django view',
      'Gives you the most control over you application logic',
      'is mapped manually to URLs',
    ]
    return Response({'message':'hello','an_appiview':an_apiview})
  
  def post(self, request):
    """Create a hello message with our name"""
    serializer= self.serializer_class(data=request.data)
    if serializer.is_valid():
      name= serializer.validated_data.get('name')
      message= f'Hello {name}'
      return Response({'message': message})
    else:
      return Response(
        serializer.errors, 
        status=status.HTTP_400_BAD_REQUEST
        )

  def put(self,request,pk=None):
    """Handle updating an object"""
    return Response({'method': 'PUT'})
  
  def patch(self,request,pk=None):
    """Handle a partial update of an object"""
    return Response({'method': 'PATCH'})

  def delete(self,request,pk=None):
    """Delete an object"""
    return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
  """ Test API ViewSet """
  serialier_class= serializer.HelloSerializer

  def list(self, request):
    """Return hello message"""
    a_viewset=[
      'Uses actions (list, create, retrieve, update,partial_update)',
      'Automatically maps to URLs using Routers',
      'Provides more functionality with less code'
    ]
    return Response({'message': 'Hello!','a_viewset':a_viewset})
  
  def create(self, request):
    """Create a new hello message"""
    serializer= self.serializer_class(data=request.data)
    if serializer.is_valid():
      name= serializer.validated_data.get('name')
      message= f'Hello {name}'
      return Response({'message': message})
    else:
      return Response(
        serializer.errors, 
        status=status.HTTP_400_BAD_REQUEST
        )
  
  def retrieve(self, request,pk=None):
    """Handle getting an object by its ID"""
    return Response({'http_method':'GET'})
  
  def update(self, request,pk=None):
    """Handle updating an object """
    return Response({'http_method':'PUT'})

  def partial_update(self,request,pk=None):
    """Handle updating part of an object """
    return Response({'http_method':'PATCH'})
  
  def destroy(self,request,pk=None):
    """Handle destroy an object """
    return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
  """Handle creating and updating profiles"""
  serializer_class = serializer.UserProfileSerializer
  queryset = models.UserProfile.objects.all()
  authentication_classes = (TokenAuthentication,)
  permission_classes = (permissions.UpdateOwnProfile,)
  filter_backends=(filters.SearchFilter,)
  search_fields=('name','email',)

class UserLoginApiView(ObtainAuthToken):
  """Handle creating user autehntication tokens"""
  renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

