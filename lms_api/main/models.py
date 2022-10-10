from django.db import models

# Create your models here.


# Teacher Model
class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=180)
    password = models.CharField(max_length=20)
    qualification = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self) -> str:
        return self.full_name


# Course Category Model
class CourseCategory(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.title


# Course Model
class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


# Student Model
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=180)
    password = models.CharField(max_length=20)
    qualification = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    address = models.TextField()
    interested_categories = models.TextField()

    def __str__(self) -> str:
        return self.full_name