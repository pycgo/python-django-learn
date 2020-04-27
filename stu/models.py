from django.db import models

# Create your models here.
#定义学生类的模型 用于建表
class Student(models.Model):
    sname = models.CharField(max_length=30, unique=True)
    spwd = models.CharField(max_length=30)
    #自定义表名 如果不写 默认是app+模型的类名（小写） 这里是stu_student
    # class Meta:
    #     db_table = 't_tu'

    #定义数据展示效果  不用了  用admin的类继承改一下 参见admin.py
    # def __str__(self):
    #     return u'Student:%s'%self.sname


