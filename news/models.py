from django.db import models
from tinymce import models as tinymce_models
from django.utils.text import slugify
from django.urls import reverse



# Create your models here.
class News(models.Model):
    # information
    title = models.CharField('Title', max_length = 256)
    image = models.ImageField("Image", upload_to = 'media/news_images')
    description = tinymce_models.HTMLField('Description', max_length = 2000)
    slug = models.SlugField('Slug', max_length = 256, unique = True, editable = False)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_details', kwargs = {'slug': self.slug})

    def get_uniqe_slug(self):
        slug = slugify(self.title.replace('ə', 'e'))
        unique_slug = slug
        counter = 1
        while News.objects.filter(slug = unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug
    
    def save(self, *args, **kwargs):
        self.slug = self.get_uniqe_slug()
        return super(News, self).save(*args, **kwargs)


