from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from library import views
from django.contrib import admin

router = DefaultRouter()
router.register(r'notes', views.NoteViewSet,
                basename='note'),
router.register(r'books', views.BookViewSet,
                basename='book'),
router.register(r'users', views.UserViewSet,
                basename='user'),
router.register(r'featured/books', views.FeaturedBooksViewSet,
                basename='featured-books')
router.register(r'profile', views.UserProfileViewSet, basename='profile')
router.register(r'user/read', views.UserReadViewSet, basename='read')
router.register(r'user/reading', views.UserReadingViewSet, basename='reading')
router.register(r'user/want', views.UserWantToReadViewSet,
                basename='want-to-read')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('/api/accounts/', include('drf_registration.urls')),
    path('', include(router.urls)),
]
