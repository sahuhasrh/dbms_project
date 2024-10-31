from django.db import models

class Department(models.Model):
    dept_name = models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    is_lab = models.BooleanField(default=False)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    hours_per_week = models.IntegerField()

    def __str__(self):
        return self.subject_name

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.faculty_name

class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.IntegerField()  # 0=Monday, 6=Sunday

    def __str__(self):
        return f"{self.day_of_week}: {self.start_time} - {self.end_time}"

class TimeTable(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.subject} - {self.faculty}"
