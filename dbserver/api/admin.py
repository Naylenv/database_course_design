from django.contrib import admin
from .models import *

# class PostAdmin(admin.ModelAdmin):
#     list_display = ['title', 'created_time',
#                     'modified_time', 'student', 'author']  # 列表页展示的字段
#     # fields = ['title', 'body', 'excerpt', 'student', 'tags']  # 表单中展现的字段

#     def save_model(self, request, obj, form, change):
#         obj.author = request.user
#         super().save_model(request, obj, form, change)


class ElectiveAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'score', 'retake']  # 列表页展示的字段
    # fields = ['title', 'body', 'excerpt', 'student', 'tags']  # 表单中展现的字段


class AwardAdmin(admin.ModelAdmin):
    list_display = ['student', 'style', 'time']  # 列表页展示的字段


class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'name', 'teacher', 'department']  # 列表页展示的字段


class Act_StuAdmin(admin.ModelAdmin):
    list_display = ['student', 'activity']  # 列表页展示的字段


class Com_StuAdmin(admin.ModelAdmin):
    list_display = ['student', 'competition']  # 列表页展示的字段


class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'classroom_id']


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'department_id']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'student_id']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher_id']


class ActivityAdmin(admin.ModelAdmin):
    list_display = ['activity_id', 'name']


class CompetitionAdmin(admin.ModelAdmin):
    list_display = ['competition_id', 'name']


class ExamAdmin(admin.ModelAdmin):
    list_display = ['exam_id', 'name', 'course', 'time', 'address']

    # fields = ['title', 'body', 'excerpt', 'student', 'tags']
# admin.site.register(Post, PostAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Admin)
admin.site.register(Elective, ElectiveAdmin)
admin.site.register(Act_Stu, Act_StuAdmin)
admin.site.register(Com_Stu, Com_StuAdmin)
