from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics, permissions
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer

# Django REST Framework has several generic views that are helpful. We have already used 
# ListAPIView in both the Library and Todos APIs to create a read-only endpoint collection, 
# essentially a list of all model instances. In the Todos API we also used RetrieveAPIView for a
# read-only single endpoint, which is analogous to a detail view in traditional Django.

# For our Blog API we want to list all available blog posts as a read-write endpoint which means
# using ListCreateAPIView, which is similar to the ListAPIView we’ve used previously but allows
# for writes. We also want to make the individual blog posts available to be read, updated, or
# deleted. There is a built-in generic Django REST Framework view just for this purpose:
# RetrieveUpdateDestroyAPIView.

# # PostList uses the generic ListCreateAPIView
# class PostList(generics.ListCreateAPIView):
#     # To restrict access to our data at the view level (one way to do it), we import permissions in our view at the top, then define it within our views as per below.
#     # The issue with doing the views based permissions is that as a project grows we need to constantly add new lines of code to add restrictions. This can be avoided it we do it at a project level. See settings for global auth changes.
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
    
# PostDetail uses the RetrieveUpdateDestroyAPIView
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
    
#     # In views.py we import IsAuthorOrReadOnly and then add the permission classes to PostDetail (extension of permissions.py to allow adming all access vs common user or no user)
#     # We import IsAuthorOrReadOnly from our permissions.py module.
#     permission_classes = (IsAuthorOrReadOnly,)
    
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# # A class that lists out all the users
# class UserList(generics.ListCreateAPIView):
#     # We need to reference the users model to get access to the users themselves so we import get_user_model to reference our User model.
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# # A class that provides a detail view of an individual user
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer



# The above views have a lot of repetition in their code (same queryset and serializer_class). To clean up the code we can import viewset instead of generic and update the code as per below.

# ModelViewSet provides both a list view and a detail view for us so it's much concise then using the generics views where we list each of them out.
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer