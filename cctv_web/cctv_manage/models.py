from django.db import models

# Create your models here.

class User(models.Model):
    password = models.CharField("비밀번호",max_length=20,null=True)

class File_list(models.Model):
    file_name = models.CharField("파일 명",max_length=50,null=False)