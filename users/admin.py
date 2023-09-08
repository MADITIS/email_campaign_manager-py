from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Subscriber


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'first_name',
                    'is_staff', 'is_superuser')
    search_fields = ('email', 'first_name', )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('user', 'subscribed_campaigns')
    list_filter = ('subscribed_campaigns',)
    search_fields = ('user__email', 'user__first_name')

    def subscribed_campaigns(self, obj):
        return ", ".join([campaign.subject for campaign in obj.subscribed_campaigns.all()])
