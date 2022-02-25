from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from instagramapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', views.sort_items),
    path('hi/<str:name>/<int:age>', views.say_hi),
    path('posts/', include('posts.urls')),
    path('users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 