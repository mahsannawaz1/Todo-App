from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('create/<str:pk>',views.c_product,name='create'),
     path('edit/<str:pk>',views.u_product,name='product-update'),
     path('',views.list_products,name='home'),
     path('list/<str:pk>',views.list_product,name='list'),
     path('delete/<str:pk>',views.delete_product,name='delete')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

