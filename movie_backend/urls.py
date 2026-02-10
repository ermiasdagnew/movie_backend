from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simple home view for the root URL
def home(request):
    return HttpResponse("🎬 Movie Recommendation Backend is live! Visit /api/movies/ to see movies.")

urlpatterns = [
    # Root path shows a simple message
    path('', home, name='home'),

    # Admin panel
    path('admin/', admin.site.urls),

    # Movies API
    path('api/movies/', include('movies.urls')),

    # Swagger documentation (if you have it set up)
    path('swagger/', include('swagger.urls')),  # remove if you don't have swagger app
]
