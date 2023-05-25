from django.urls import path
from django.contrib import admin
from .views import home
from .views import signup
from .views import buy
from .views import login_view
from .views import nueva_pieza
from .views import mi_coleccion
from .views import mostrar, compra, eliminar, eliminar_form, editar, editarForm, help_editing


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mostrar , name='mostrar'),
    path('signup/', signup , name='register'),
    path('home/', home , name='home'),
    path('buy/', compra, name='buy' ),
    path('login/', login_view, name= 'login_view'),
    path('create/', nueva_pieza, name='nueva_pieza'),
    path('mycollection/', mi_coleccion, name='mi_coleccion'),
    path('mycollection/eliminar/',eliminar,name='eliminar' ),
    path('mycollection/editar/',editarForm,name='editar' ),
    path('mycollection/eliminarform/',eliminar_form,name='eliminar_form' ),
    path('mycollection/editarid/',editarForm,name='help_editing'),
    path('mycollection/editarid/editarform/',editarForm,name='editarForm' ),
]
