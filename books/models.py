from django.db import models

class Books(models.Model):
    name= models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name
    
    Year_of_publication = models.DateTimeField()