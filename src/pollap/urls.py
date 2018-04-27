from django.contrib import admin
from django.urls import path
from django.urls import include
from pollap.apps.website.views import LandingView

urlpatterns = [
    path('', LandingView.as_view(), name="landing"),
    path('admin/', admin.site.urls)
]
