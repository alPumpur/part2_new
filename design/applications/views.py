from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, CreateApplicationForm
from .models import *


def index(request):
    num_applications = Application.objects.filter(status_app__exact='П').count()
    num_complete = Application.objects.filter(status_app__exact='В').order_by('-date_app')[:4]
    context = {
        'num_applications': num_applications,
        'num_complete': num_complete
    }
    return render(request, 'applications/index.html', context)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'applications/register.html'
    success_url = reverse_lazy('login')


@login_required()
def UserProfile(request):
    status_filter = request.GET.get('status_app', 'all')

    if status_filter == 'all':
        applications = Application.objects.filter(user=request.user).order_by('-date_app')
    else:
        applications = Application.objects.filter(user=request.user, status_app=status_filter).order_by('-date_app')

    context = {
        'applications': applications,
        'status_filter': status_filter,
    }

    return render(request, 'applications/profile.html', context)


class CreateApplicationView(CreateView):
    form_class = CreateApplicationForm
    template_name = 'applications/create_application.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateApplicationView, self).form_valid(form)


class DeleteApplicationView(DeleteView):
    model = Application
    template_name = 'applications/delete_application.html'
    success_url = reverse_lazy('profile')
