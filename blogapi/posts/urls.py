from django.urls import path
# from .views import UserList, UserDetail, PostList, PostDetail
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet

# urlpatterns = [
#     path("users/", UserList.as_view()),
#     path("users/<int:pk>/", UserDetail.as_view()),
#     # PostDetail view (also to be written) at api/v1/# where # represents the primary key of the entry
#     path("<int:pk>/", PostDetail.as_view()),
#     # All blog routes will be at api/v1/ so our PostList view has the empty string "" will be at api/v1 /
#     path("", PostList.as_view()),
# ]

# Routers work directly with viewsets to automatically generate URL patterns for us. Our current urls, above, has four URL patterns. Two for blog posts and two for users. We can instead adopt a single rout for each viewset. So two routes instead of four URL patterns.

# Django REST Framework has two default routers: SimpleRouter and DefaultRouter. We will use SimpleRouter (import at top) but it’s also possible to create custom routers for more advanced functionality.

# Setting the router to user SimpleRouter
router = SimpleRouter()
# Register each viewset for Users and Posts
router.register("users", UserViewSet, basename="users")
router.register("", PostViewSet, basename="posts")

# Set our URLs to use the new router
urlpatterns = router.urls

