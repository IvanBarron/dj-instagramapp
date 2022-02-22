from django.contrib import admin
from django.urls import path
from instagramapp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', views.sort_items),
    path('hi/<str:name>/<int:age>', views.say_hi),
]
