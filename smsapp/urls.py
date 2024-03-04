from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path('cars', views.CarsDetails.as_view(), name='cars_details'),
    path('planes', views.PlanesDetails.as_view(), name='planes_details'),
    path('send', views.send, name='send'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
