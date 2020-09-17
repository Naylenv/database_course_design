from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags
# Create your models here.


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200, blank=True)
    # cid = models.CharField(max_length=50)
    #person_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:  # admin 中配置
        verbose_name = '学院'
        verbose_name_plural = verbose_name


class Classroom(models.Model):
    classroom_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    #person_id = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:  # admin 中配置
        verbose_name = '班级'
        verbose_name_plural = verbose_name


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=20, blank=True)
   # user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    phone_num = models.CharField(max_length=20, blank=True)
    person_id = models.CharField(max_length=20, blank=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:  # admin 中配置
        verbose_name = '学生'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=20, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    person_id = models.CharField(blank=True, max_length=20)
    age = models.IntegerField(null=True, blank=True)
    phone_num = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:  # admin 中配置
        verbose_name = '教师'
        verbose_name_plural = verbose_name


class Competition(models.Model):
    competition_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True)
    # style = models.CharField(max_length=200, blank=True)
    info = models.CharField(max_length=100, blank=True)
    organizer = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:  # admin 中配置
        verbose_name = '比赛'
        verbose_name_plural = verbose_name


class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    info = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    organizer = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:  # admin 中配置
        verbose_name = '活动'
        verbose_name_plural = verbose_name


class Course(models.Model):
    course_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:  # admin 中配置
        verbose_name = '课程'
        verbose_name_plural = verbose_name


class Elective(models.Model):
    elective_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    retake = models.IntegerField(default=0)
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.student.name

    class Meta:  # admin 中配置
        verbose_name = '选课'
        verbose_name_plural = verbose_name


class Exam(models.Model):
    exam_id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, max_length=100)
    time = models.CharField(max_length=100)
    # date = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    course = models.ForeignKey(
        Course, blank=True, null=True,  on_delete=models.CASCADE)

    def __str__(self):
        if self.course is not None:
            return self.course.name
        else:
            return self.name

    class Meta:  # admin 中配置
        verbose_name = '考试'
        verbose_name_plural = verbose_name


class Award(models.Model):
    award_id = models.AutoField(primary_key=True)
    style = models.CharField(max_length=200)
    content = models.CharField(max_length=100, blank=True)
    time = models.DateTimeField(default=timezone.now)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    flag = models.IntegerField()

    def __str__(self):
        return self.style

    class Meta:  # admin 中配置
        verbose_name = '奖惩信息'
        verbose_name_plural = verbose_name


class Act_Stu(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name

    class Meta:  # admin 中配置
        verbose_name = '活动报名'
        verbose_name_plural = verbose_name


class Com_Stu(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name

    class Meta:  # admin 中配置
        verbose_name = '比赛报名'
        verbose_name_plural = verbose_name


class Admin(models.Model):
    id = models.IntegerField(primary_key=True)
    pwd = models.CharField(max_length=40)
    nickname = models.CharField(max_length=20)
    email = models.CharField(max_length=40, blank=True)
    modified_time = models.DateTimeField()
    created_time = models.DateTimeField(default=timezone.now)
    usertype = models.IntegerField(default=2)
    # rid = models.ForeignKey(Role)

    def __str__(self):
        return self.nickname

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
# class Post(models.Model):

#     # 文章标题
#     title = models.CharField(max_length=70)

#     body = models.TextField()

#     created_time = models.DateTimeField(default=timezone.now)
#     modified_time = models.DateTimeField()
#     excerpt = models.CharField(max_length=200, blank=True)
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     tags = models.ManyToManyField(Tag, blank=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = '文章'
#         verbose_name_plural = verbose_name
#         ordering = ['-created_time']

#     def save(self, *args, **kwargs):
#         self.modified_time = timezone.now()
#         md = markdown.Markdown(extensions=[
#             'markdown.extensions.extra',
#             'markdown.extensions.codehilite',
#         ])
#         self.excerpt = strip_tags(md.convert(self.body))[:54]
#         super().save(*args, **kwargs)

#     def get_absolute_url(self):
#         return reverse('student:detail', kwargs={'pk': self.pk})
