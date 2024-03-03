from django.db import models
from ..players.db_queries import get_team_queryset


class Match(models.Model):
    team_1_ids = models.CharField(
        max_length=255
    )
    team_2_ids = models.CharField(
        max_length=255
    )
    match_date = models.DateField(
        auto_now_add=True,
    )

    def get_team_1(self):
        return get_team_queryset(self.team_1_ids)

    def get_team_2(self):
        return get_team_queryset(self.team_2_ids)
