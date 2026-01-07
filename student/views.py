from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import ListView, CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
from .forms import StudentForms
from .models import Student
from django.contrib.auth.mixins import LoginRequiredMixin
class StudentListCreateView( LoginRequiredMixin,ListView):
    model = Student
    form_class = StudentForms
    template_name = 'student/student.html'
    context_object_name = 'students'
    success_url = reverse_lazy('student')
    login_url = 'login'
    def get_queryset(self):
        return Student.objects.all() 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context
    def post(self, request ,  *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return self.get(request)
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForms
    template_name = 'student/student_update.html'
    success_url = reverse_lazy('student')
class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('student')
