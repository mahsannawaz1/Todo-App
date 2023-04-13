from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
   
    path('user/',userForm,name='register'),
    path('profile/',userProfile,name='profile'),
    path('login/',LoginView.as_view(template_name='users/userlogin.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='users/userlogout.html'),name='logout'),
    path('update/<str:pk>',userUpdate,name='update')

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
