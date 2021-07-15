from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Genre(models.Model):
    genre_name = models.CharField(max_length=20)

    def __str__(self):
        return self.genre_name

class Language(models.Model):
    language_name = models.CharField(max_length=20)

    def __str__(self):
        return self.language_name

class Form(models.Model):
    book_name = models.CharField(max_length=80, validators=[MinLengthValidator(2)])
    author_name = models.CharField(max_length=80, validators=[MinLengthValidator(2)])
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    language = models.ForeignKey(Language,on_delete=models.CASCADE)


    def __str__(self):
        return self.author_name
        return self.book_name
