from django.db import models


DESCRIPTIONS = (
    (0,"sunny"),
    (1,"Rain"),
    (3,"Cloudy"),
    (4,"Snow")
)

class Description(models.Model):
    description = models.IntegerField(choices=DESCRIPTIONS,default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()

    def __str__(self):
        return str(self.description)
    
    class Meta:
        ordering = ['-created_on']
