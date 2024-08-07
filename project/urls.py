
from django.contrib import admin
from django.urls import path, include
from prestamosapp import views
from django.conf import settings#ESTO ES PARA PODER VISUALIZAR LAS FOTOS
from django.conf.urls.static import static #ESTO ES PARA PODER VISUALIZAR LAS FOTOS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio, name='inicio'),
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('', views.cliente_list, name='cliente_list'),
    path('prestamosapp/', include('prestamosapp.urls', namespace='prestamosapp')),
    
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #ESTO ES PARA PODER VISUALIZAR LAS FOTOS

