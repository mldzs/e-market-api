from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from ..celery import app


@app.task(name="enviar_email_task")
def enviar_email(to: list, subject: str, context: dict, template: str) -> None:
    from_email: str = settings.DEFAULT_FROM_EMAIL

    html_content = render_to_string(template, context)
    text_content = strip_tags(html_content)

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
