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

    def __str__(self):
        return self.name    