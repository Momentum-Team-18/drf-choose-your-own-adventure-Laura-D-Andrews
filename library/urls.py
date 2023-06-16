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
# router.register(r'users/admin', views.UserAdminViewSet, basename='user-admin'),
# router.register(r'private/profile',
#                 views.UserPrivateProfileViewSet, basename='user-private'),
# router.register(r'public/profile',
#                 views.UserPublicProfileViewSet, basename='user-public'),
# router.register(r'notes', views.NoteViewSet, basename='notes'),
# router.register(r'books', views.BookBasicInfoViewSet, basename='book'),
# router.register(r'book/profile',
#                 views.BookDetailedProfileViewSet, basename='book-profile'),
# router.register(r'books/featured', views.BookFeaturedViewSet, basename='book-featured'),

# router = DefaultRouter()
# router.register(r'users', views.UserBasicViewSet,
#                 basename='user'),
# router.register(r'users/details', views.UserAllTheDetailsViewSet,
#                 basename='users-details'),
# router.register(r'books', views.BookViewSet, basename='book'),
# router.register(r'notes', views.NoteBasicViewSet, basename='note'),
# router.register(r'note/details', views.NoteAllTheDetailsViewSet,
#                 basename='note-details')
# router.register(r'user/notes', views.UserNotesViewset, basename='users-notes')

# user basic, user detail, book, note basic, note detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    # path('accounts/', include('registration.backends.simple.urls')),
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
