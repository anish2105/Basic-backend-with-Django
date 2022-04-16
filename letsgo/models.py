from django.db import models

class details(models.Model):
    name = models.CharField(max_length= 30)
    email = models.CharField(max_length= 30)
    views = models.CharField(max_length = 30)

    def __str__(self):
        return "%s %s"%(self.name,self.views)
