from django.db import models
from api.models import Student, Admin
from django.utils import timezone


class Discuss(models.Model):
    discuss_id = models.AutoField(primary_key=True)
    text = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    like_num = models.IntegerField(default=0)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text[:10]

    class Meta:
        verbose_name = '帖子'
        verbose_name_plural = verbose_name


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    text = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    discuss = models.ForeignKey(Discuss, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:10]

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
# Create your models here.
