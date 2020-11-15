from django.db import models

# Create your models here.
class Images(models.Model):
    name = models.CharField(max_length = 60)
    image=models.ImageField(upload_to ='images/')
    description = models.TextField()
    image_location = models.ForeignKey('Location', on_delete=models.CASCADE,)
    image_category = models.ForeignKey('Category', on_delete=models.CASCADE,)
    
    @classmethod
    def save_image(self):
        self.save()

    @classmethod
    def delete_image(self):
        self.delete()

    @classmethod
    def filter_by_location(cls,location):
        images_location = cls.objects.filter(image_location_name=location)
        return images_location

    @classmethod 
    def get_all_images(cls):
        images=cls.objects.all()
        return images

    def __str__(self):
        return self.name    

class Location(models.Model):
    locations=(
        ('England','England'),
        ('France','France'),
        ('Germany','Germany'),
        ('Italy','Italy'),
        ('Spain','Spain'),
    )
    imglocs = models.CharField(max_length = 255, choices = locations)
    
    def __str__(self):
        return f"{self.imglocs}"