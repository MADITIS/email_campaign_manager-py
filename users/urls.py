from django.contrib import admin
from django.urls import path
from .views import add_subscriber

urlpatterns = [
    path("subscribe/<int:campaign_id>", add_subscriber, name="add_sub"),
]
