from posixpath import basename
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from base.views import *
# from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
from base.views import MyTokenObtainPairView


router = routers.DefaultRouter()
# router.register('users', UserViewSet, basename='user')
router.register('artist', ArtistViewSet, basename='artist')
router.register('painting', PaintingViewSet, basename='painting')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('base.urls')),
    path('user/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
