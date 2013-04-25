from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=120)
    content = models.TextField()

    def __unicode__(self):
        return self.name
