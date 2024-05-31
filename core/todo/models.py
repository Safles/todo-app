from django.db import models

# Create your models here.
class todoLIST(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=200)
    deadline = models.DateField()
    def __str__(self):
        return str(self.id)