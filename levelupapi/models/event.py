from django.db import models


class Event(models.Model):
    """Event Model
    Fields:
        organizer (ForeignKey): the user that made the event
        game (ForeignKey): the game associated with the event
        date (DateField): The date of the event
        time (TimeFIeld): The time of the event
        description (TextField): The text description of the event
        title (CharField): The title of the event
        attendees (ManyToManyField): The gamers attending the event
    """

    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    description = models.TextField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='events')
    date = models.DateTimeField()
    time = models.TimeField()
    title = models.CharField(max_length=100)
    attendees = models.ManyToManyField("Gamer", through="EventGamer", related_name='attending')


    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value

    @property
    def attendees_count(self):
        return self.__attendees_count
    # @property
    # def attendee_count(self):
    #     length = len(self.attendees.all())
    #     return length

    @attendees_count.setter
    def attendees_count(self, value):
        self.__attendees_count = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        self.__owner = value

