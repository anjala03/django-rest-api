from django.db import models

# Create your models here.
class Colors(models.Model):
    color_name=models.CharField(max_length=15)
    color_used=models.TextField()
    color_code=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.color_name

class People(models.Model):
    #adding the foreign key from the Colors table
    just_color=models.ForeignKey(Colors, related_name="colorsss", null=True, blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=100, verbose_name="Full_Name")
    age=models.IntegerField()
    sex=models.CharField(max_length=10, verbose_name="Gender")

    def __str__(self) -> str:
        return self.name
    class Meta:
        ordering=["name"]



