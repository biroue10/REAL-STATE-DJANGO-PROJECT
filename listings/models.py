from django.db import models


class Listing(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.TextField()
    # image = models.ImageField()

    def __str__(self) -> str:
        return self.title
