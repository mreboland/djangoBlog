"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # It is a good practice to always version your APIs—v1/, v2/, etc—since when you make a large
    # change there may be some lag time before various consumers of the API can also update. That
    # way you can support a v1 of an API for a period of time while also launching a new, updated v2
    # and avoid breaking other apps that rely on your API back-end.
    # If we had multiple apps in a project it might make more sense to create a dedicated api app and then include all the other API url routes into it. But because this is basic, we'll directly include our posts app here.
    path("api/v1/", include("posts.urls")),
    # To avoid having to go to the admin page to log in and out while testing, we can add the below line of code which will add the log in and out functionality directly to the browsable API itself. It'll add a log our button in a dropdown to the username at the top right of the screen.
    path("api-auth/", include("rest_framework.urls")),
    # Adding our 3rd party app to urls so we can access it.
    # We go to : http://127.0.0.1:8000/api/v1/dj-rest-auth/login or:
    # http://127.0.0.1:8000/api/v1/dj-rest-auth/logout/ to do so. There is also /password/reset for pswd reset and /password/reset/confirm for confirmation page.
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")),
    # http://127.0.0.1:8000/api/v1/dj-rest-auth/registration/
    # Gives us a user registration endpoint at the above address
    path("api/v1/dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
]
