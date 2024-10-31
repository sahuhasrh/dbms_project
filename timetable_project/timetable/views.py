from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.http import HttpResponseRedirect
from .models import Department, TimeTable, TimeSlot
from .forms import SubjectForm, FacultyForm

def home(request):
    return render(request, 'timetable/home.html')

def view_timetable(request):
    dept_id = request.GET.get('department')
    if not dept_id:
        departments = Department.objects.all()
        return render(request, 'timetable/select_department.html', {'departments': departments})

    timetable = TimeTable.objects.filter(subject__dept_id=dept_id).select_related(
        'slot', 'subject', 'faculty'
    ).order_by('slot__day_of_week', 'slot__start_time')

    time_slots = TimeSlot.objects.filter(
        start_time__lt='16:30:00'
    ).exclude(
        start_time__range=('12:30:00', '13:29:59')
    ).order_by('start_time')

    timetable_grid = {}
    for entry in timetable:
        day = entry.slot.day_of_week
        time = entry.slot.start_time
        if time not in timetable_grid:
            timetable_grid[time] = {}
        timetable_grid[time][day] = entry

    context = {
        'time_slots': time_slots,
        'timetable_grid': timetable_grid,
        'days': range(1, 6),  # Monday to Friday
        'department': Department.objects.get(id=dept_id)
    }

    return render(request, 'timetable/view_timetable.html', context)

class SubjectCreateView(View):
    def get(self, request):
        form = SubjectForm()
        return render(request, 'timetable/add_subject.html', {'form': form})

    def post(self, request):
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subject added successfully.')
            return redirect('timetable:view_timetable')  # Updated to match new URL name
        return render(request, 'timetable/add_subject.html', {'form': form})

class FacultyCreateView(View):
    def get(self, request):
        form = FacultyForm()
        return render(request, 'timetable/faculty_form.html', {'form': form})

    def post(self, request):
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Faculty added successfully.')
            return redirect('timetable:view_timetable')  # Updated to match new URL name
        return render(request, 'timetable/faculty_form.html', {'form': form})

def generate_timetable(request):
    # Logic for generating the timetable will go here
    # For now, we'll just show a simple message
    if request.method == 'POST':
        messages.success(request, 'Timetable generated successfully!')
        return redirect('timetable:view_timetable')  # Updated to match new URL name
    return render(request, 'timetable/generate_timetable.html')
