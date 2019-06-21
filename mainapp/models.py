from django.db import models

# Create your models here.

class Project(models.Model):
    project_title = models.CharField(max_length = 150)
    pub_date = models.DateTimeField('date published')
    project_url = models.URLField(max_length = 200)
    project_description = models.TextField()
    project_title_image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.project_title


class DisplayImage(models.Model):
    Image_description = models.CharField(max_length = 500)
    Image = models.ImageField(upload_to = 'carousel_images/')
