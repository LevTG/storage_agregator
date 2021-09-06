from django.db import models
import uuid
from colorfield.fields import ColorField


class Line(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    color = ColorField(default='#FF0000')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Station(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    line = models.ForeignKey(Line, related_name='stations', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    code_name = models.CharField(max_length=100, default=line.name+name)

    def __str__(self):
        return self.name

    @property
    def color(self):
        return self.line.color
