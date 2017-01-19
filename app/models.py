from __future__ import unicode_literals

from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100, default="unknown")
    father_name = models.CharField(max_length=100, default="unknown")
    district = models.CharField(max_length=100,)
    date_added = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def get_episodes_per_season(self):
        return list(self.episode.all())

    def death_season(self):
        return EpisodePerSeason.objects.filter(character=self, died_here=True).first()


class EpisodePerSeason(models.Model):
    name = models.CharField(max_length=100)
    character = models.ForeignKey(Character, related_name="episode")
    died_here = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
