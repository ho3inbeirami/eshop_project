
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

# settings.py add :

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL_USE_TLS = True

# EMAIL_HOST ='smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER= 'test@gmail.com'
# EMAIL_HOST_PASSWORD= '*******'

## active less secure apps in google.com


def Send_email(subject,to, context, template_name):
    try:
        html_message= render_to_string(template_name, context)
        print(html_message)
            
        plain_message= strip_tags(html_message)
        print(plain_message)
        from_email = settings.EMAIL_HOST_USER
        print(from_email)
        send_mail(subject,plain_message ,from_email, [to], html_message)

        print('DONE')
    except:
        pass
    
 




