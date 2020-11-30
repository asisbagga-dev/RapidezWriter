from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404

from .models import Database, Category
from .forms import Databaseform, Categoryform
from django.db.models import Q

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
def resume_makeover_3(request):
    return render(request,"resumeMakeover3.html")

def resume_video(request):
    return render(request,"resume_video.html")

def linkedin(request):
    return render(request,"linkedin.html")

def create_blog(request):
    forms = Databaseform()
    if request.method == "POST":
        forms = Databaseform(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'createBlog.html', {'form': forms})


# Career Advise List Pages
def career_list_page(request):
    all_objects = Database.objects.all()
    return render(request, 'career_list.html', {"objects": all_objects})

def career_detail_page(request, pk):
    category = Category.objects.all()
    blog = get_object_or_404(Database, pk=pk)
    return render(request, "career_detail.html",  {"blog_details":blog, "category":category})


def blog_update(request, pk):
    blog = get_object_or_404(Database, pk=pk)
    forms = Databaseform(request.POST or None, instance = blog)
    if request.method == "POST":
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect(reverse( 'career_detail_page', args=[pk]))
        else:
            print(forms.errors.as_data())
    return render(request, "blogUpdate.html", {"forms":forms})  

# Delete a Blog
def blog_delete(request, pk):
    obj = get_object_or_404(Database, pk=pk)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(reverse('career_list_page'))
    return render(request, 'blogDelete.html')


def career_view_all_page(request):
    return render(request, "career_view_all.html")

# Categories

def add_category(request):
    forms = Categoryform()
    if request.method == "POST":
        forms = Categoryform(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'createBlogCategory.html', {'form': forms})

def category_list_page(request):
    all_objects = Category.objects.all()
    return render(request, 'category_list.html', {"objects": all_objects})

def delete_category(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(reverse('career_list_page'))
    return render(request, 'blogDeleteCategory.html', {"obj":obj})

def view_category_wise(request, filter):
    category = Category.objects.all()
    filter = get_object_or_404(Category, category=filter)
    filter_op = Database.objects.filter(category=filter)
    return render(request, 'career_view_all.html', {'filter_op':filter_op, "filter":filter, "category":category})