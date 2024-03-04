from django.shortcuts import render
from .models import Car, Plane
from django.views.generic import View
from .mix_file import ObjectMixin
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


# def cars_details(request):
#     car_objects = Car.objects.all()
#     return render(request, 'cars.html', {'cars': car_objects})


# def planes_details(request):
#     plane_objects = Plane.objects.all()
#     return render(request, 'planes.html', {'planes': plane_objects})


# class CarsDetails(View):
#     def get(self, request):
#         car_objects = Car.objects.all()
#         return render(request, 'cars.html', {'cars': car_objects})
#
#
# class PlanesDetails(View):
#     def get(self, request):
#         plane_objects = Plane.objects.all()
#         return render(request, 'planes.html', {'planes': plane_objects})

class CarsDetails(ObjectMixin, View):
    model = Car
    template = 'cars.html'


class PlanesDetails(ObjectMixin, View):
    model = Plane
    template = 'planes.html'


def send(request):
    if request.method == 'POST':
        title = request.POST['title']
        message = request.POST['message']
        address = request.POST['email']
        send_mail(title, message, 'settings.EMAIL_HOST_USER', [address],
                  fail_silently=False)

    return render(request, 'send_email.html')
