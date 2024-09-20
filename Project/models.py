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
    POSITION_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('fullstack', 'Fullstack'),
    ]
    
    title = models.CharField(max_length=100)
    project_link = models.TextField()
    slug = AutoSlugField(populate_from='title')
    description = models.TextField()
    role = models.CharField(max_length=20, choices=POSITION_CHOICES, default='frontend')
    technologies = models.ManyToManyField(Technology)
    image = models.ImageField(upload_to = 'project-banner-image')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        try:
            # Get the existing project object from the database
            this = Project.objects.get(id=self.id)
            # If a new image is uploaded, delete the old one
            if this.image != self.image:
                this.image.delete(save=False)
        except Project.DoesNotExist:
            pass  # This means it's a new object, so no previous image to delete

        super(Project, self).save(*args, **kwargs)
    
    
    

