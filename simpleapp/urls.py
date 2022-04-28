from django.urls import path

from simpleapp.api import views

app_name = 'simpleapp'

urlpatterns = [
    path(
        route='api/',
        view=views.SimpleListCreateView.as_view(),
        name='simple_rest_api'
    ),
    path(
        route='api/<slug:slug>/',
        view=views.SimpleRetrieveUpdateDestroyAPIView.as_view(),
        name='simple_rest_api'
    )
]

