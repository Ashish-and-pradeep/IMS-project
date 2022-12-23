from django.contrib import admin
from .models import Student,Teacher,Course,Teachers,Gall,Content
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','branch','year','email','password','address','image','gender']
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name','branch','email','password','qualification','address','gender','contact','image']

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['desc','image']
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course','image']
class TeachersAdmin(admin.ModelAdmin):
    list_display = ['name','desc','image']
class ContentAdmin(admin.ModelAdmin):
    list_display = ['name','subject','content']
admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Gall,GalleryAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Teachers,TeachersAdmin)
admin.site.register(Content,ContentAdmin)