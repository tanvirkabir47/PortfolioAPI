from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Technology(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "Technologies"
    
    def __str__(self):
        return self.name
    
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField()
    technologies = models.ManyToManyField(Technology)
    image = models.ImageField(upload_to = 'project-banner-image')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.title
    
    
    

