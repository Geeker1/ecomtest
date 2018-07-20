from django.views.decorators.http import require_POST
from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from contact.tasks import send_feedback_email_task


def contact(request):
    form = ContactForm()
    return render(request,'contact.html',{'form':form})



@require_POST
def contact_save(request):
    data = dict()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data['form_is_valid'] = True
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject,message, from_email, ['admin@frozine.com'])
                send_feedback_email_task.delay(from_email)
            except BadHeaderError:
                return HttpResponse('Invalid Header Found!!')
            form = ContactForm()
        else:
            data['form_is_valid'] = False
            
                
    else:
        form = ContactForm()
    
    context = {'form': form}
    data['html_contact_form'] = render_to_string('includes/contact_update.html', context, request=request)
    return JsonResponse(data)
