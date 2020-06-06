from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from fcm_django.models import FCMDevice

from ..celery import app


@app.task(name="enviar_email_task")
def enviar_email(to: list, subject: str, context: dict, template: str) -> None:
    from_email: str = settings.DEFAULT_FROM_EMAIL

    html_content = render_to_string(template, context)
    text_content = strip_tags(html_content)

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@app.task(name="enviar_notificacao_task")
def enviar_notificacao(id_usuarios: list, title: str, body: str, data: dict = None):
    devices = FCMDevice.objects.filter(user_id__in=id_usuarios)
    devices.send_message(title=title, body=body, data=data)
