from concurrent.futures import ThreadPoolExecutor
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from users.models import Subscriber
from django.conf import settings


def send_email(email_data):
    subject, recipient, message = email_data
    send_mail(subject, strip_tags(message), settings.EMAIL_HOST_USER,
              [recipient], html_message=message)


def send_daily_campaigns():
    subscribers = Subscriber.objects.filter(is_active=True)

    max_workers = 4
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        email_tasks = []

        for subscriber in subscribers:
            for campaign in subscriber.subscribed_campaigns.all():
                html_message = render_to_string(
                    'campaign.html', {'campaign': campaign})

                email_task = (
                    campaign.subject,
                    subscriber.user.email,
                    html_message,
                )
                email_tasks.append(email_task)
                executor.submit(send_email, email_task)

    print("All emails sent")
