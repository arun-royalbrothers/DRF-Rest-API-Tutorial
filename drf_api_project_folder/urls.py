"""
URL configuration for drf_api_project_folder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework import permissions
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="DRF Tutorial",
        default_version='v1',
        description="DRF Tutorial",
    ),
    public=True,
)


#To check the sentry debug mode
def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), #this from drf official website
    path('', include('mainApp.urls')),
    path('api/hello-world-api/', include('helloWorld.urls')),
    path('api/employee-details-api/', include('employeeDetails.urls')),
    path('api/student-details-api/', include('StudentDetails.urls')),
    path('api/todo-api/', include('TodoApp.urls')),
    path('api/voters-details-api/', include('votersDetails.urls')),
    path('api/spotify-api/', include('spotifyApp.urls')),
    path('api/blog-api/', include('BlogApp.urls')),
    path('api/books-api/', include('booksApp.urls')),
    path("api/movie-review-api/", include('MovieReviewApp.urls')),
    path('api/music-api/', include('MusicAPI.urls')),
    path('api/recipe-api/', include('RecipeApp.urls')),
    path('api/library-api/', include('LbraryApp.urls')),
    path('api/advanced-methods-api/', include('advancedMethods.urls')),
    path("api/server/", include("server_health_check.urls")),
    path('sentry-debug/', trigger_error), #to check the sentry debug mode
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
