from django.urls import path
from .views import *
app_name='nflapp'
urlpatterns = [
    path('jugadores/<int:pk>/', JugadorDetailView.as_view(), name='detalle_jugador'),
    path('jugadores/<int:pk>/editar/', JugadorUpdateView.as_view(), name='editar_jugador'),
    path('jugadores/<int:pk>/eliminar/', JugadorDeleteView.as_view(), name='eliminar_jugador'),
    path('jugadores/nuevo/', JugadorCreateView.as_view(), name='nuevo_jugador'),

    path('equipos/<int:pk>/', EquipoDetailView.as_view(), name='detalle_equipo'),
    path('equipos/<int:pk>/editar/', EquipoUpdateView.as_view(), name='editar_equipo'),
    path('equipos/<int:pk>/eliminar/', EquipoDeleteView.as_view(), name='eliminar_equipo'),
    path('equipos/nuevo/', EquipoCreateView.as_view(), name='nuevo_equipo'),

    path('eventos/<int:pk>/', EventoDetailView.as_view(), name='detalle_evento'),
    path('eventos/<int:pk>/editar/', EventoUpdateView.as_view(), name='editar_evento'),
    path('eventos/<int:pk>/eliminar/', EventoDeleteView.as_view(), name='eliminar_evento'),
    path('eventos/nuevo/', EventoCreateView.as_view(), name='nuevo_evento'),

    path('estadios/<int:pk>/', EstadioDetailView.as_view(), name='detalle_estadio'),
    path('estadios/<int:pk>/editar/', EstadioUpdateView.as_view(), name='editar_estadio'),
    path('estadios/<int:pk>/eliminar/', EstadioDeleteView.as_view(), name='eliminar_estadio'),
    path('estadios/nuevo/', EstadioCreateView.as_view(), name='nuevo_estadio'),

    path('propietarios/<int:pk>/', PropietarioDetailView.as_view(), name='detalle_propietario'),
    path('propietarios/<int:pk>/editar/', PropietarioUpdateView.as_view(), name='editar_propietario'),
    path('propietarios/<int:pk>/eliminar/', PropietarioDeleteView.as_view(), name='eliminar_propietario'),
    path('propietarios/nuevo/', PropietarioCreateView.as_view(), name='nuevo_propietario'),
    path('', IndexView.as_view(), name='index'),
]

