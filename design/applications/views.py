from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm
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
