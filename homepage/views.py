from django.shortcuts import render, redirect
from django.contrib import messages
from .models import PersonalInfo
from .forms import PersonalInfoForm

def home(request):
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your information has been added successfully!')
            return redirect('home')  # Redirect to avoid re-submission on refresh
        else:
            if 'captcha' in form.errors:
                messages.error(request, 'Please complete the CAPTCHA verification.')
            else:
                messages.error(request, 'Please correct the errors below.')
    else:
        form = PersonalInfoForm()
    
    return render(request, 'homepage/index.html', {
        'form': form
    })

def projects(request):
    all_projects = PersonalInfo.objects.all().order_by('-id')  # Show newest first
    return render(request, 'homepage/projects.html', {
        'all_projects': all_projects
    })

def project_detail(request, project_id):
    try:
        project = PersonalInfo.objects.get(id=project_id)
    except PersonalInfo.DoesNotExist:
        from django.http import Http404
        raise Http404("Project does not exist")
    return render(request, 'homepage/project_detail.html', {
        'project': project
    })