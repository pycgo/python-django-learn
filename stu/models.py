from django.db import models

# Create your models here.
#定义学生类的模型 用于建表
class Student(models.Model):
    sname = models.CharField(max_length=30, unique=True)
    spwd = models.CharField(max_length=30)

    # class Meta:
    #     db_table = 't_tu'


