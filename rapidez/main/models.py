from django.db import models

# Create your models here.
class Database(models.Model):
    heading = models.CharField(max_length=300)
    description = models.TextField()
    banner = models.ImageField(upload_to='images', blank = True)

    def __str__(self):
        return self.heading
