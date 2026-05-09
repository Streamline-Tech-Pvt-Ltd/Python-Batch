from django.db import models

# Create your models here.
class Interns(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    s_date = models.DateField()
    e_date = models.DateField()
    
def __str__(self):
    return self.name

class Meta:
    db_table = 'Interns'