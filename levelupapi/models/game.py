from django.db import models


class Game(models.Model):
    """Game Model
    Fields:
        models (CharField): The name of the game
        game_type (ForeignKey): The type of game
        description (CharField): The description of the game
        number_of_players (IntegerField): The max number of players of the game
        maker (CharField): The company that made the game
    """

    title = models.CharField(max_length=100)
    maker = models.CharField(max_length=50)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='games')
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField(default=0)

    @property
    def event_count(self):
        return self.__event_count

    @event_count.setter
    def event_count(self, value):
        self.__event_count = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        self.__owner = value

    @property
    def user_event_count(self):
        return self.__user_event_count

    @user_event_count.setter
    def user_event_count(self, value):
        self.__user_event_count = value
