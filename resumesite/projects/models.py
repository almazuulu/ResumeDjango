from django.db import models
from users.models import Profile
import uuid

# Create your models here
class Project(models.Model):
    owner = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Название Проекта')
    description = models.TextField(null = True, blank=True, verbose_name='Описание проекта') #blank means we can submit withou being be filled
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    demo_link = models.CharField(max_length= 2000, null=True, blank=True, verbose_name='Демо ссылка')
    source_link = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Ссылка на проект')
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='Тэги')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания') #generate autimcally date
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False) #16 char string nums and letters
    vote_total = models.IntegerField(default=0, null=True, blank=True, verbose_name='Итого голосов')
    vote_ratio = models.IntegerField(default=0, null=True, blank=True, verbose_name='Соотношение голосов')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = "Проекты"

        ordering = ['created']
        #ordering = ['-created'] - Сортировка по убыванию

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )

    #owner =
    project = models.ForeignKey(Project, on_delete = models.CASCADE, verbose_name='Проект')
    body = models.TextField(null=True, blank = True, verbose_name='Отзыв')
    value = models.CharField(max_length=200, choices = VOTE_TYPE, verbose_name='Значение')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')  # generate autimcally date
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,
                          editable=False)  # 16 char string nums and letters

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя тэга')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания тэга')  # generate autimcally date
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,
                          editable=False)  # 16 char string nums and letters

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

