from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simple home view for '/'
def home(request):
    return HttpResponse("🎬 Movie Recommendation Backend is live! Visit /api/movies/ to see movies.")

urlpatterns = [
    # Root path
    path('', home, name='home'),

    # Admin panel
    path('admin/', admin.site.urls),

    # Movies API
    path('api/movies/', include('movies.urls')),  # Make sure movies app has urls.py
]
