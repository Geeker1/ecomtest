from django.core.mail import send_mail, BadHeaderError

def send_feedback_email(email):
    """
    Task to send an email notification when a contact is made.
    """

    subject = 'SignUp'
    message = 'You have successfully signed up to our platform'
    mail_sent = send_mail(subject,message,'admin@froxine.com',[email])
    return mail_sent