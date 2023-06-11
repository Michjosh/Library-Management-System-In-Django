# from django.urls import path, include
# from rest_framework.routers import SimpleRouter
# from .import views
#
# router = SimpleRouter()
# router.register('authors', views.AuthorViewSet)
# router.register('authors', views.BookViewSet)
# print(router.urls)
#
# urlpatterns = [
#     path('', include(router)),
# ]
#

from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from .import views

router = DefaultRouter()
router.register('authors', views.AuthorViewSet)
router.register('books', views.BookViewSet)
print(router.urls)

urlpatterns = [
    path('', include(router.urls)),
    path('sendmail/', views.sendMailFunction)
]
