from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from library import views
from django.contrib import admin

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'books', views.BookViewSet, basename='book')
router.register(r'notes', views.NoteViewSet, basename='note')
# router.register(r'user/books', views.UserBooksViewSet, basename='user-books')
# router.register(r'user/notes', views.UserNotesViewSet, basename='user-notes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('users/', views.user_list, name="user-list"),
#     path('users/<int:pk>', views.user_detail, name='user-detail'),
#     path('books/', views.book_list, name='book-list'),
#     path('books/<int:pk>', views.book_detail, name='book-detail'),
#     path('notes/', views.note_list, name="note-list"),
#     path('notes/<int:pk>', views.note_details, names="note-detail"),
#     path('user/books/<int:pk>', views.user_books, name="user-books")
#     path('user/notes/<int:pk>', views.user_notes, name='user-notes')
# ]
