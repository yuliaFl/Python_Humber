from django.db import models

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


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    semester = models.IntegerField()
    courses_enrolled = models.ForeignKey(CompletedCourse, on_delete=models.CASCADE, null=True)
    courses_completed =models.ForeignKey(OngoingCourse, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name
