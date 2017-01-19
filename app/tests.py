import datetime
from django.test import TestCase
from app.models import Character, EpisodePerSeason


class TestCharacter(TestCase):
    def setUp(self):
        Character.objects.create(name='TMCG', date_added=datetime.date.today())

    def test_character_with_no_mother(self):
        character = Character.objects.first()
        self.assertEquals(character.mother_name, "unknown")

    def test_get_episodes_per_season(self):
        character = Character.objects.first()
        appearance = EpisodePerSeason.objects.create(name="2 Episodes in Season 1", character=Character.objects.first())
        self.assertEquals(character.get_episodes_per_season(), [appearance])

    def test_season_of_death(self):
        character = Character.objects.first()
        appearance1 = EpisodePerSeason.objects.create(name="2 Episodes in Season 1", character=Character.objects.first()
                                                      )
        appearance2 = EpisodePerSeason.objects.create(name="4 Episodes in Season 2", character=Character.objects.first()
                                                      )
        appearance1.died_here = False
        appearance2.died_here = True
        appearance2.save()

        self.assertEquals(character.death_season(), appearance2)


class TestEpisodePerCharacter(TestCase):
    pass
