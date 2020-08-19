from django.shortcuts import render
from django.views.generic import TemplateView
from configure import models as config_models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
import os
import socket


# Create your views here.


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'monitor/index.html'
    x = config_models.Armstate.objects.get(pk=1)
    z = config_models.Lockstate.objects.get(pk=1)

    def get_context_data(self, **kwargs):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = str(s.getsockname()[0])
        port =':8081'
        stream_address = ip + port.replace(' ', '')
        self.x.refresh_from_db()
        s.close()
        self.z.refresh_from_db()
        if str(self.x) == "1":
            arm_state = "Enabled"
            arm_color = "text-success"
        elif str(self.x) == "0":
            arm_state = "Disabled"
            arm_color = "text-danger"
        else:
            arm_state = "Error"
            arm_color = "text-primary"

        if str(self.z) == "1":
            lock_state = "Locked"
            lock_color = "text-success"
        elif str(self.z) == "0":
            lock_state = "Unlocked"
            lock_color = "text-danger"
        else:
            lock_state = "Error"
            lock_color = "text-primary"
        if os.name == 'posix':
            ip = os.popen('hostname -I').read()
        filepath = settings.MEDIA_ROOT + '/log.txt'
        file = open(filepath, "r")
        log = file.readlines()
        log = log[-10::]
        log.reverse()
        context = super().get_context_data(**kwargs)
        context['log'] = log
        context['monitor_active'] = 'active'
        context['armstate'] = arm_state
        context['armcolor'] = arm_color
        context['lockstate'] = lock_state
        context['lockcolor'] = lock_color
        context['ip'] = stream_address
        return context
