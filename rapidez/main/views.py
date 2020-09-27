from django.shortcuts import render

# Home Page

def home(request):
    return render(request,"home.html")

# About the company Pages
def about(request):
    return render(request,"about.html")

def contact_us(request):
    return render(request,"contact.html")

def testimonials(request):
    return render(request,"testimonials.html")

# Service Pages
def resume_consulting(request):
    return render(request,"resume_consulting.html")

def resume_writing(request):
    return render(request,"resume_writing.html")

def resume_makeover(request):
    return render(request,"resume_makeover.html")
def resume_makeover_1(request):
    return render(request,"resume_makeover1.html")
def resume_makeover_2(request):
    return render(request,"resume_makeover2.html")

def resume_video(request):
    return render(request,"resume_video.html")

def linkedin(request):
    return render(request,"linkedin.html")


# Career Advise List Pages
def career_list_page(request):
    return render(request, "career_list.html")

def career_detail_page(request):
    return render(request, "career_detail.html")

def career_view_all_page(request):
    return render(request, "career_view_all.html")

