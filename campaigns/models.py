from django.db import models

# app_label = "email_campaign_manager"


class Campaign(models.Model):
    subject = models.CharField(max_length=255)
    preview_text = models.CharField(max_length=255)
    article_url = models.URLField()
    html_content = models.TextField()
    plain_text_content = models.TextField()
    published_date = models.DateField()

    def __str__(self):
        return self.subject
