from .views import (
    PlayersIndexView,
    PlayerDetailView,
    PlayerCreateView,
    PlayerUpdateView,
    PlayerDeleteView,
    AddToRosrerView,
)
from django.urls import path


urlpatterns = [
    path('', PlayersIndexView.as_view(), name='players_index'),
    path('<int:pk>/', PlayerDetailView.as_view(), name='player_details'),
    path('create/', PlayerCreateView.as_view(), name='player_create'),
    path('<int:pk>/update/', PlayerUpdateView.as_view(), name='player_update'),
    path('<int:pk>/delete/', PlayerDeleteView.as_view(), name='player_delete'),
    path(
        '<int:pk>/add_to_roster/',
        AddToRosrerView.as_view(),
        name='add_to_roster'
    ),
]
