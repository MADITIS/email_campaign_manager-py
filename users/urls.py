from django.contrib import admin
from django.urls import path
from .views import add_subscriber, unsubscribe

urlpatterns = [
    path("subscribe/<int:campaign_id>", add_subscriber, name="sub"),
    path("unsubscribe/<int:campaign_id>", unsubscribe, name="unsub"),
]
