from django.contrib import admin
from .models import Car, Plane, Comment

# Register your models here.
admin.site.register(Car)
admin.site.register(Plane)
admin.site.register(Comment)