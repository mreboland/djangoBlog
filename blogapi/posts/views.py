from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# Django REST Framework has several generic views that are helpful. We have already used 
# ListAPIView in both the Library and Todos APIs to create a read-only endpoint collection, 
# essentially a list of all model instances. In the Todos API we also used RetrieveAPIView for a
# read-only single endpoint, which is analogous to a detail view in traditional Django.

# For our Blog API we want to list all available blog posts as a read-write endpoint which means
# using ListCreateAPIView, which is similar to the ListAPIView we’ve used previously but allows
# for writes. We also want to make the individual blog posts available to be read, updated, or
# deleted. There is a built-in generic Django REST Framework view just for this purpose:
# RetrieveUpdateDestroyAPIView.

# PostList uses the generic ListCreateAPIView
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
# PostDetail uses the RetrieveUpdateDestroyAPIView
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
