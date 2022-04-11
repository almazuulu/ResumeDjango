from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False) #16 char string nums and letters
    name = models.CharField(max_length=200, null = True, blank=True, verbose_name='ФИО')
    username = models.CharField(max_length=200, null=True, blank=True, verbose_name='Логин')
    email = models.CharField(max_length=200, null=True, blank=True, verbose_name='Почтовый адрес')
    short_intro = models.CharField(max_length=250, blank=True, null=True, verbose_name='Краткая информациия')
    bio = models.TextField(blank=True, null=True, verbose_name='Биография')
    profile_image = models.ImageField(null=True, blank=True, default='profiles/user-default.png', upload_to='profiles/')
    social_github = models.CharField(max_length=250, blank=True, null=True, verbose_name='Профиль в GitHub')
    social_twitter = models.CharField(max_length=250, blank=True, null=True, verbose_name='Профиль в Twitter')
    social_youtube = models.CharField(max_length=250, blank=True, null=True, verbose_name='Профиль в YouTube')
    social_facebook = models.CharField(max_length=250, blank=True, null=True, verbose_name='Профиль в Facebook')
    social_linkedin = models.CharField(max_length=250, blank=True, null=True, verbose_name='Профиль в LinkedIn')
    personal_website = models.CharField(max_length=250, blank=True, null=True, verbose_name='Персональный сайт')
    location = models.CharField(max_length=200, blank=True, null=True,verbose_name='Текущее местоположе')


    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Skill(models.Model):
    owner = models.ForeignKey(Profile, blank=True, null=True, on_delete = models.CASCADE, verbose_name ='Разработчик')
    name = models.CharField(max_length=150, blank=True, null=True, verbose_name= 'Наименование')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    id = models.UUIDField(default=uuid.uuid4, unique=True, blank=True, primary_key=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'