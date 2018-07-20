
from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Your Email', required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(
        max_length=2000,
        widget = forms.Textarea(),
        help_text='Write your Message..'
    )