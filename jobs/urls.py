from django.urls import path, include
from . import views 
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('create', csrf_exempt(views.create_job), name="create-job"),
    path('all', csrf_exempt(views.get_all_jobs), name="all"),
    path('employee-accept-job', csrf_exempt(views.employee_accept_job), name="employee_accept_job"),
    path('employer-accept-employee', csrf_exempt(views.employer_accept_employee), name="employer_accept_employee"),
    path('get-all-job-qeued-users', csrf_exempt(views.get_all_job_qeued_users), name="get_all_job_qeued_users"),
    path('employer-decline-employee', csrf_exempt(views.employer_decline_employee), name="employer_decline_employee"),
    path('edit_job',csrf_exempt(views.edit_job), name="edit_job" ),
]
