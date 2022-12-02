from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=5)
    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=5)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class PlatoComida(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to ='myapp/static/assets/platos_comida/')
    price = models.DecimalField(decimal_places=2, max_digits=5)
    rating = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(5)])
    
    def __str__(self):
        return self.name