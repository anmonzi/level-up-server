from django.db import models


class EventGamer(models.Model):
    """Join model for Events and Gamers
    """

    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='attendees')
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
