from django.contrib import admin
from django.urls import path

from debt_site import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.DebtView.as_view()),
]
