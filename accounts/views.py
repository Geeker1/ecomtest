from django.shortcuts import render,redirect,reverse
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.template.loader import render_to_string
from .tasks import send_feedback_email_task
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login




def signup(request):
    data = dict()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data['form_is_valid'] = True
            email = form.cleaned_data['email']
            user = form.save()
            send_feedback_email_task.delay(email)
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
    return render(request, 'accounts/signup.html', {'form':form})