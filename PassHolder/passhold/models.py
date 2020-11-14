from django.db import models


class Data(models.Model):
    title = models.CharField(verbose_name="Title", max_length=32, unique=True)
    login = models.CharField(verbose_name="Login/Email", max_length=32)
    password = models.CharField(verbose_name="Password", max_length=64)
    note = models.TextField(verbose_name="Note", max_length=255, null=True)

    def __str__(self):
        return self.title
