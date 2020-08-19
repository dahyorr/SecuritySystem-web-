from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from . import forms


# Create your views here.

@login_required
def index(request):
    template_name = 'profiles/index.html'
    error = ""
    if request.method == "POST" and request.POST.get('form') == "edit-profile":
        form1 = forms.UserForm(data=request.POST, instance=request.user)
        if form1.is_valid():
            form1.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('Profile:Index')
        else:
            messages.error(request, 'Please correct the error below')
            error = 'profile'
    else:
        form1 = forms.UserForm(instance=request.user)

    if request.method == 'POST' and request.POST.get('form') == "edit-password":
        form2 = PasswordChangeForm(request.user, request.POST)
        if form2.is_valid():
            password = form2.save()
            update_session_auth_hash(request, password)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('Profile:Index')
        else:
            messages.error(request, 'Please correct the error below')
            error = 'password'
    else:
        form2 = PasswordChangeForm(request.user)

    context = {'form1': form1, 'form2': form2, 'error': error, }
    return render(request, template_name, context)



