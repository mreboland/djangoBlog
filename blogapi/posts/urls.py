from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    # PostDetail view (also to be written) at api/v1/# where # represents the primary key of the entry
    path("<int:pk>/", PostDetail.as_view()),
    # All blog routes will be at api/v1/ so our PostList view has the empty string "" will be at api/v1 /
    path("", PostList.as_view()),
]
