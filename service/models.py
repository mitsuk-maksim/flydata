from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField("Имя", max_length=100)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField("Сообщение")
