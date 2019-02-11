from django.db import models


# Create your models here.
class TimeStampedObjectModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, )
    updated_on = models.DateTimeField(auto_now=True, )

    class Meta:
        abstract = True


class Stock(TimeStampedObjectModel):
    name = models.CharField(max_length=128, blank=False, unique=True, )
    symbol = models.CharField(max_length=32, blank=False, unique=True, db_index=True, )
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{0} [{1}]".format(self.symbol, self.name)
