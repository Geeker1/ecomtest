from django.core.mail import send_mail, BadHeaderError

def send_feedback_email(from_email):
    """
    Task to send an email notification when a contact is made.
    """

    subject = 'Contact Review'
    message = 'Hello, there your message has been received and we are reviewing it right now...\n You would be contacted shortly'
    mail_sent = send_mail(subject,message,'admin@froxine.com',[from_email])
    return mail_sent

