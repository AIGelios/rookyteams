from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    CreateView, UpdateView, DeleteView,
    DetailView, View, ListView, TemplateView,
)
from django_filters.views import FilterView
from .models import Player
from .db_queries import (
    add_to_roster, delete_from_roster, clear_roster,
)
from .forms import PlayerForm
from .filters import PlayerFilterSet
from rooky_teams.mixins import SuccessMessageMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.db import IntegrityError


SUCCESS_URL = reverse_lazy('players_index')


class PlayersIndexView(FilterView):
    template_name = 'players/index.html'
    model = Player
    filterset_class = PlayerFilterSet

    def get_queryset(self):
        return super().get_queryset().order_by('first_name')


class PlayerRosterView(ListView):
    template_name = 'players/roster.html'
    model = Player

    def get_queryset(self):
        return (
            super().get_queryset()
            .filter(is_in_roster=True)
            .order_by('first_name')
        )


class PlayerDetailView(DetailView):
    template_name = 'players/details.html'
    model = Player


class PlayerCreateView(SuccessMessageMixin, CreateView):
    template_name = 'players/create.html'
    model = Player
    form_class = PlayerForm
    success_url = SUCCESS_URL
    success_message = _('Player successfully added!')


class PlayerUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'players/update.html'
    model = Player
    form_class = PlayerForm
    success_url = SUCCESS_URL
    success_message = _('Player successfully updated!')


class PlayerDeleteView(SuccessMessageMixin, DeleteView):
    template_name = 'players/delete.html'
    model = Player
    success_url = SUCCESS_URL
    success_message = _('Player successfully deleted from database')


class AddToRosrerView(View):
    def post(self, request, *args, **kwargs):
        success_message = _('Player successfully added to the next match')
        error_message = _('Error. Cannot add player to roster!')
        try:
            player_id = kwargs.get('pk')
            add_to_roster(player_id)
            messages.success(self.request, success_message)
        except IntegrityError:
            messages.error(self.request, error_message)
        return redirect(SUCCESS_URL)


class DeleteFromRosterView(View):
    def post(self, request, *args, **kwargs):
        success_message = _('Player successfully removed from roster')
        error_message = _('Error. Cannot remove player from roster!')
        try:
            player_id = kwargs.get('pk')
            delete_from_roster(player_id)
            messages.success(self.request, success_message)
        except IntegrityError:
            messages.error(self.request, error_message)
        return redirect(reverse_lazy('roster'))


class RosterClearView(TemplateView):
    template_name = 'players/clear_roster.html'

    def post(self, request, *args, **kwargs):
        success_message = _('Roster successfully cleared')
        error_message = _('Error. Cannot clear roster!')
        try:
            clear_roster()
            messages.success(self.request, success_message)
        except IntegrityError:
            messages.error(self.request, error_message)
        return redirect(reverse_lazy('players_index'))
