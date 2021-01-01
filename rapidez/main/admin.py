from django.contrib import admin
from .models import Database, Category, Testimonials

# Register your models here.
admin.site.register(Database)
admin.site.register(Category)
admin.site.register(Testimonials)