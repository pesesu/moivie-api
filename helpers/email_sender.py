from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

from django.conf import settings

class Mail:
    @staticmethod
    def send_template_mail(
        template,
        context,
        subject,
        from_email=settings.EMAIL_HOST_USER,
        to_email_list=[]
    ):
        try:
            html_body = render_to_string(template, context)
            text_body = strip_tags(html_body)
            message = EmailMultiAlternatives(
                subject= subject,
                from_email= from_email,
                to= to_email_list,
                body= text_body
            )
            message.attach_alternative(html_body, 'text/html')
            message.send()
        except Exception as e:
            raise ValueError(e)