from django.urls import path, include
from . import views 
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('create', csrf_exempt(views.create_job), name="create-job"),
    path('all', csrf_exempt(views.get_all_jobs), name="all"),
]
