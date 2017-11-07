from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

class Activity(models.Model):
    UP_VOTE = 'U'
    DOWN_VOTE = 'D'
    LIKE = 'L'
    ACTIVITY_TYPES = (
        (UP_VOTE, 'Up Vote'),
        (DOWN_VOTE, 'Down Vote'),
        (LIKE, 'Like')
    )

    user = models.ForeignKey(to = 'User')
    activity_type = models.CharField(max_length = 1, choices = ACTIVITY_TYPES)
    date_and_time = models.DateTimeField(auto_now_add = True)

    # Generic Foreign Key area
    content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        unique_together = ("content_type", "object_id")
        #добавить уникальности с Meta

class Book(models.Model):
    #При поиске конкретной книги перебираются все, индекс ускорит
    title = models.CharField(verbose_name='Название', max_length = 255, db_index = True)
    creation_date = models.DateField(verbose_name='Дата написания')
    authors = models.ManyToManyField(to = 'Writer', verbose_name = 'Авторы')
    genre = models.ForeignKey(to = 'Genre', verbose_name = 'Жанр')
    votes = GenericRelation(Activity)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

class Review(models.Model):
    user = models.ForeignKey(to = 'User', verbose_name = 'Пользователь')
    book = models.ForeignKey(to = 'Book', verbose_name = 'Книга')
    content = models.TextField(verbose_name = 'Содержимое')
    date_of_creation = models.DateTimeField(auto_now_add = True, verbose_name = 'Время написания')
    likes = GenericRelation(Activity)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Writer(models.Model):
    name = models.CharField(verbose_name = 'Имя', max_length = 255)
    date_of_birth = models.DateField(verbose_name = 'Дата рождения', blank = True, null = True)
    date_of_death = models.DateField(verbose_name = 'Дата смерти', blank = True, null = True)
    votes = GenericRelation(Activity)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Писатель'
        verbose_name_plural = 'Писатели'

class Genre(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class User(models.Model):
    nickname = models.CharField(verbose_name = 'Никнейм', max_length = 30)
    date_of_registration = models.DateField(verbose_name = 'Дата регистрации', db_index = True)
    votes = GenericRelation(Activity)

    def __str__(self):
        return self.nickname

    class Meta:
        ordering = ('date_of_registration', )
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

# Create your models here.
