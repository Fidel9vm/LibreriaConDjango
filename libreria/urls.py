from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear, name='crear'),
    path('libros/editar', views.editar, name='editar'),
    path('libros/editar/<int:id>', views.editar, name='editar'),
    path('eliminar/<int:id>  ', views.eliminar, name='eliminar'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('signin/', views.signin, name='signin'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)