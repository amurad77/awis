from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
class Projects(models.Model):
    # information
    title = models.CharField('Title', max_length = 256)
    image = models.ImageField("Image", upload_to = 'media/projects_images')
    description = tinymce_models.HTMLField('Description', max_length = 2000)
    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title