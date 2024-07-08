from django.contrib import admin
from django.urls import path
from findobj.views import detection, get_users_images, index, delete
from user.views import LoginView, logout_user, RegisterView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='base'),

    # users path
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),

    # findobj path
    path('myimg/', get_users_images, name='get_users_images'),
    path('detection/', detection, name='detection'),
    path('delete/<str:pk>/',
         delete, name="image_delete"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
