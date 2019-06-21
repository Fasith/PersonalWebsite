from django.db import models

# Create your models here.

class Project(models.Model):
    project_title = models.CharField(max_length = 150)
    pub_date = models.DateTimeField('date published')
    project_url = models.URLField(max_length = 200)
    project_decription = models.TextField()
    project_title_image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.project_title