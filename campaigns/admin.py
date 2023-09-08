from django.contrib import admin
from .models import Campaign


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('subject', 'published_date')
    search_fields = ('subject', 'preview_text', 'published_date')
