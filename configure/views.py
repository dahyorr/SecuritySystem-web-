from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from . import forms
import socket
import os
import datetime
from uptime import uptime
red_led = 21
green_led = 20
blue_led = 16
door_lock = 4
red_state = blue_state = green_state = door_state =  0
if os.name == 'posix':
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(red_led, GPIO.OUT)
    GPIO.setup(green_led, GPIO.OUT)
    GPIO.setup(blue_led, GPIO.OUT)
    GPIO.setup(door_lock, GPIO.OUT)


def gpio_update():
    global red_state, blue_state, green_state, door_state
    if os.name == 'posix':
        red_state = GPIO.input(red_led)
        blue_state = GPIO.input(blue_led)
        green_state = GPIO.input(green_led)
        door_state = GPIO.input(door_lock)
    else:
        red_state = 0
        blue_state = 0
        green_state = 0
        door_state = 0


@login_required
def index(request):
    rfids = models.RfidId.objects.all()
    users = User.objects.all()
    x = models.Armstate.objects.get(pk=1)
    if request.method == "POST" and request.POST.get("form") == 'rfid':
        select_rfid = []
        for item in rfids:
            if request.POST.get(item.ownername) is not None:
                select_rfid.append(request.POST.get(item.ownername))
        for item in select_rfid:
            models.RfidId.objects.filter(pk=int(item)).delete()
        messages.success(request, 'Tag deleted successfully')
        return redirect('/manage/#rfid')

    if request.method == "POST" and request.POST.get("form") == 'user':
        select_user = []
        for item in users:
            if request.POST.get(item.username) is not None:
                select_user.append(request.POST.get(item.username))
            print(select_user)
        for item in select_user:
            User.objects.filter(pk=int(item)).delete()
        messages.success(request, 'User deleted successfully')
        return redirect('/manage/#users')

    if request.method == "POST" and request.POST.get("form") == 'changepin':
        current_pin = str(request.POST.get("currentpin"))
        new_pin = str(request.POST.get("newpin"))
        confirm_pin = str(request.POST.get("confirmpin"))
        if len(current_pin) != 6 or len(new_pin) != 6:
            messages.error(request, 'PIN must be a 6 digit number')
            return redirect('/manage/#pin')
        else:
            try:
                int(current_pin)
                int(new_pin)
                int(confirm_pin)
            except ValueError:
                messages.error(request, 'PIN must be a 6 digit number')
                return redirect('/manage/#pin')
            pin_code = models.Pincode.objects.get(pk=1)
            pin_code.refresh_from_db()
            pin = str(pin_code)
            if current_pin != pin:
                messages.error(request, 'The Pin you entered is incorrect')
                return redirect('/manage/#pin')
            else:
                if new_pin != confirm_pin:
                    messages.error(request, 'The Pin you entered does not match')
                    return redirect('/manage/#pin')
                else:
                    if current_pin == new_pin:
                        messages.warning(request, 'The new pin cannot be the same as the old one')
                        return redirect('/manage/#pin')
                    else:
                        new_pin = int(new_pin)
                        pin_code.code = new_pin
                        pin_code.save()
                        messages.success(request, 'The PIN has been changed successfully')
                        return redirect('/manage/')

    if os.name == 'posix':
        ip = os.popen('hostname -I').read()

    else:
        ip = 'Not Supported'

    hostname = socket.gethostname()
    x.refresh_from_db()
    sysuptime = str(datetime.timedelta(seconds=round(uptime())))

    if str(x) == "1":
        arm_state = "Enabled"
        arm_color = "text-success"
    elif str(x) == "0":
        arm_state = "Disabled"
        arm_color = "text-danger"
    else:
        arm_state = "Error"
        arm_color = "text-primary"

    rfids = models.RfidId.objects.all()
    template_name = 'configure/index.html'
    gpio_update()
    context = {
        "manage_active": "active",
        'users': users,
        'rfids': rfids,
        'hostname': hostname,
        'ip': ip,
        'armstate': arm_state,
        'armcolor': arm_color,
        'uptime': sysuptime,
        'red_state': red_state,
        'green_state': green_state,
        'blue_state': blue_state,
        'door_state': door_state,
    }
    return render(request, template_name, context)


class NewTag(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'configure/newtag.html'
    login_url = '/login/'
    form_class = forms.RfidForm
    model = models.RfidId
    success_url = '/manage/#rfid'
    success_message = 'Tag Created Successfully'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = "New Tag"
        return context


class EditTag(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'configure/newtag.html'
    form_class = forms.RfidForm
    model = models.RfidId
    login_url = '/login/'
    success_url = '/manage/#rfid'
    success_message = 'Tag updated Successfully'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = "Edit Tag"
        return context


class NewUser(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = forms.UserCreateForm
    login_url = '/login/'
    success_url = '/manage/#users'
    template_name = 'configure/newuser.html'
    success_message = 'User Created Successfully'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = 'New User'
        return context
