from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404

from .models import Database, Category, Testimonials
from .forms import Databaseform, Categoryform, SignUpForm, Testimonialform
from django.db.models import Q

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

import razorpay

# SignUp Page
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



# General Page
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def contact_us(request):
    return render(request,"contact.html")

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
def quizes(request):
    return render(request, "quiz.html")

# Create Blog
def create_blog(request):
    forms = Databaseform()
    if request.method == "POST":
        forms = Databaseform(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'createBlog.html', {'form': forms})
# Blog Listings
def career_list_page(request):
    all_objects = Database.objects.all()
    return render(request, 'career_list.html', {"objects": all_objects})
# Blog Page details
def career_detail_page(request, pk):
    category = Category.objects.all()
    blog = get_object_or_404(Database, pk=pk)
    return render(request, "career_detail.html",  {"blog_details":blog, "category":category})
# Update Blog
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
#
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
# Categories List Page
def category_list_page(request):
    all_objects = Category.objects.all()
    return render(request, 'category_list.html', {"objects": all_objects})
# Delete Category
def delete_category(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(reverse('career_list_page'))
    return render(request, 'blogDeleteCategory.html', {"obj":obj})
# View Blog Category wise
def view_category_wise(request, filter):
    category = Category.objects.all()
    filter = get_object_or_404(Category, category=filter)
    filter_op = Database.objects.filter(category=filter)
    return render(request, 'career_view_all.html', {'filter_op':filter_op, "filter":filter, "category":category})

# Testimonials CRUD
def testimonials(request):
    all_objects = Testimonials.objects.all()
    return render(request,"testimonials.html", {'objects':all_objects})

def create_testimonial(request):
    forms = Testimonialform()
    if request.method == "POST":
        forms = Testimonialform(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect(reverse('testimonials'))
    return render(request, 'createTestimonial.html', {'form': forms})

def testimonial_update(request, pk):
    blog = get_object_or_404(Testimonials, pk=pk)
    forms = Testimonialform(request.POST or None, instance = blog)
    if request.method == "POST":
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect(reverse('testimonials'))
        else:
            print(forms.errors.as_data())
    return render(request, "testimonialUpdate.html", {"forms":forms}) 

def testimonial_delete(request, pk):
    obj = get_object_or_404(Testimonials, pk=pk)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(reverse('testimonials'))
    return render(request, 'testimonialDelete.html')

#Payment Gateway integration
def payment(request):
    if request.method == "POST":
        amount = 1

        client = razorpay.Client(auth=("rzp_live_nQOflfXhoAJfEG", "rpKTqVpjezaNxt8SWXHjqQUg"))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})

    return render(request, 'resume_makeover.html')

def payment_success(request):
    return render(request, "payment_success.html")