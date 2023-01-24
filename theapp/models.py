from django.db import models

class User(models.Model):
    name=models.CharField(max_length=20)
    id=models.CharField(max_length=10,primary_key=True)



    def __str__(self):
        return self.name


