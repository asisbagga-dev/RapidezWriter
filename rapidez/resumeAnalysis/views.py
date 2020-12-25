from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import ResumeForm
from .models import Resume

# Celery
from .tasks import sleepy, send_email

# Emails
from django.core.mail import send_mail



def resume_upload(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            # resume_analysis(form)
            return redirect('resumeAnalysis:thankyou')
    else:
            form = ResumeForm()
    return render(request, 'upload_resume.html', {'form': form})

def thankyou(request):
    return render(request, 'thankyou.html')

def resume_analysis(form):
    
    return True


def test(request):
    sleepy.delay(5)
    send_email()
    return redirect('resumeAnalysis:thankyou')
