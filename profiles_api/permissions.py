from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
  """allow users to edit their own profile"""
  def has_object_persmission(self,request, view, obj):
    """Check user is trying to edit their own profile"""
    if request.method in permissions.SAFEMETHODS:
      return True
    return obj.id == request.user.id
    