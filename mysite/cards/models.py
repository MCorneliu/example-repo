from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Card(models.Model):

    owner = models.ForeignKey(User)
    url = models.URLField()
    name = models.CharField(max_length=60)
    image = models.ImageField()
    media_type = models.CharField(max_length=35)
    created_at = models.DateTimeField('date created')

    def __repr__(self):
        return '<{} - {}>'.format(self.id, self.name)
    def __str__(self):
        return self.name