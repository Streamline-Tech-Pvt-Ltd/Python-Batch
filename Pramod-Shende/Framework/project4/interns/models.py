from django.db import models

# Create your models here.
class Intern(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
   
    def __str__(self):
         return self.name
     
    class Meta:
        db_table = 'interns'