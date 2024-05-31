from django.db import models

class wap(models.Model):
      music=models.FileField(upload_to='media')


class van(models.Model):
       image=models.ImageField(upload_to='media')
