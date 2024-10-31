

# Register your models here.
from django.contrib import admin
from .models import Department, Subject, Faculty, TimeSlot, TimeTable

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_name',)
    search_fields = ('dept_name',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'dept', 'is_lab', 'hours_per_week')
    list_filter = ('dept', 'is_lab')
    search_fields = ('subject_name',)

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('faculty_name', 'dept')
    list_filter = ('dept',)
    filter_horizontal = ('subjects',)
    search_fields = ('faculty_name',)

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'day_of_week')
    list_filter = ('day_of_week',)

@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ('subject', 'faculty', 'slot', 'room_number')
    list_filter = ('subject__dept', 'faculty')
    search_fields = ('subject__subject_name', 'faculty__faculty_name')
