# Time for our first custom permission. We have two users, testuser and the superuser account. There is one blog post in our database, which was created by the superuser.
# We want only the author of a specific blog post to be able to edit or delete it otherwise the blog post should be read-only. So the superuser account should have full CRUD access to the individual blog instance, but the regular user testuser should not.

from rest_framework import permissions

# We import permissions above and create a custom class below which extends BasePermission.
class IsAuthorOrReadOnly(permissions.BasePermission):
    
    # We are overriding the has_object_permission which is in the django source code itself (it has default values).
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        
        # If a request contains HTTP verbs included in SAFE_METHODS, a tuple containing GET, OPTIONS, and HEAD, then it is a read-only request and permission is granted.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the author of a post
        
        # Otherwise the request is for a write of some kind, which means updating the API resource so either create, delete, or edit functionality. In that case, we check if the author of the obj in question, our blog post (obj.author), matches the user making the request (request.user)
        return obj.author == request.user
    
    # In views.py we import IsAuthorOrReadOnly and then add the permission classes to PostDetail


# Setting proper permissions is a very important part of any API. As a general strategy, it is a good idea to set a strict project-level permissions policy such that only authenticated users can view the API. Then make view-level or custom permissions more accessible as needed on specific API endpoints.
