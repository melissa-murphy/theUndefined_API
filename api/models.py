from django.db import models
from uuid import uuid4


class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    char_name = models.CharField(max_length=25)
    base_health = models.IntegerField(5)
