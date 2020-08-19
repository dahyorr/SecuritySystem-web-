from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from configure import models
import os
# Create your views here.


def gui_changer(request):
    context = {}
    page = models.Gui.objects.get(pk=1)
    page.refresh_from_db()
    print(page)
    return render(request, 'gui/gui_base.html', context)


def check_page(request):
    if request.is_ajax and request.method == "POST":
        page = models.Gui.objects.get(pk=1)
        page.refresh_from_db()
        data = {
            'page': str(page),
        }
        return JsonResponse(data)
    else:
        return HttpResponse("Not allowed")


def get_content(request):
    if request.is_ajax and request.method == "POST":
        ajax_page = request.POST.get('page')
        current_dir = os.getcwd()
        if os.name == 'posix':
            os.chdir('/home/pi/SecuritySystem/gui/templates/gui')
        elif os.name == 'nt':
            os.chdir('C:\\Users\\dahyo\\PycharmProjects\\SecuritySystem\\gui\\templates\\gui')
        html = ""
        with open(ajax_page, 'r') as file:
            html = file.read().replace('\n', '')
        os.chdir(current_dir)
        data = {
            'content': html
        }
        return JsonResponse(data)
    else:
        return HttpResponse("Not allowed")
