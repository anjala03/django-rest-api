from django.db import models

# Create your models here.
class People(models.Model):
    name=models.CharField(max_length=100, verbose_name="Full_Name")
    age=models.IntegerField()
    sex=models.CharField(max_length=10, verbose_name="Gender")
    def __str__(self) -> str:
        return self.name
    class Meta:
        ordering=["name"]