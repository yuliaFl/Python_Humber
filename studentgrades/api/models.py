from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    semester = models.IntegerField()
    courses_enrolled = models.ManyToManyField('Course', related_name='enrolled_students')
    courses_completed = models.ManyToManyField('Course', related_name='completed_students', blank=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class CompletedCourse(Course):
    grade_achieved = models.CharField(max_length=2)

    def __str__(self):
        return f"{super().__str__()} - Grade: {self.grade_achieved}"

class OngoingCourse(Course):
    remaining_seats = models.IntegerField()

    def __str__(self):
        return f"{super().__str__()} - Remaining Seats: {self.remaining_seats}"