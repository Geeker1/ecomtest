from django.shortcuts import render,redirect,reverse
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.template.loader import render_to_string


def signup(request):
    data = dict()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data['form_is_valid'] = True
            user = form.save()
            login(request, user)
            data['url'] = reverse('home')
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            context = {'form': form}
            data['html_contact_form'] = render_to_string('includes/signup_update.html', context, request=request)
            return JsonResponse(data)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})