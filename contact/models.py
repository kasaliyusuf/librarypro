from django.db import models

# Create your models here.
class ContactTable(models.Model):
    Name = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=11)
    Email = models.EmailField()
    Massege = models.TextField()

    def __str__(self):
        return self.Name