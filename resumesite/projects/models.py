from django.db import models
import uuid

# Create your models here
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null = True, blank=True) #blank means we can submit withou being be filled
    demo_link = models.CharField(max_length= 2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True) #generate autimcally date
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False) #16 char string nums and letters


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = "Проекты"

