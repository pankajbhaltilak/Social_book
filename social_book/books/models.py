from django.db import models

# Create your models here.
class Books(models.Model):
    file = models.FileField(null=True, blank=True)
    file_name = models.CharField(max_length=254)
    description = models.CharField(max_length=300)
    visibility = models.BooleanField(default=True)
    Year_of_published = models.PositiveBigIntegerField(null=True, blank=True)
    Cost = models.PositiveBigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.file_name
