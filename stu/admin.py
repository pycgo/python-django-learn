from django.contrib import admin
from .models import Student

# Register your models here.


#新建一个类  继承admin  然后把数据展示效果改成列表
class StudentAdmin(admin.ModelAdmin):
    list_display = ('sname', 'spwd')

admin.site.register(Student,StudentAdmin)
