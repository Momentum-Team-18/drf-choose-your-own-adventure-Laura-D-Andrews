from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from library import views
from django.contrib import admin

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'books', views.BookViewSet, basename='book')
router.register(r'notes', views.NoteViewSet, basename='note')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
