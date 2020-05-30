from django.urls import path, include
from . import views 
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('login', csrf_exempt(views.login), name="get-token"),
    path('signup', csrf_exempt(views.signup), name="signup"),
    path('get-previous-jobs', views.previous_jobs, name="previous_jobs"),
    path('my-created-jobs', views.my_created_jobs, name="my_create_jobs"),
]
