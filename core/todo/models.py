from django.db import models

# Create your models here.
class todoLIST(models.Model):
    id = models.AutoField(primary_key=True)
    status=models.BooleanField(default=False)
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=200)
    priority = models.CharField(max_length=6, null=True)
    deadline = models.DateField()
    def __str__(self):
        return str(self.id)