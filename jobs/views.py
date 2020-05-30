from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
import json
from .models import Job
import datetime
from .serializers import JobSerializer


def get_user(request):
    try:
        token = str(request.META['HTTP_AUTHORIZATION']).split(' ')[1]
        user = User.objects.get(auth_token=token)
        return user
    except:
        return False


# Create your views here.
def create_job(request):
    user = get_user(request)
    if user == False:
        return JsonResponse({'error': 'User not found'})
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    
    try:
        job = Job(
            title=body['title'],
            description = body['description'],
            start_date = datetime.datetime.strptime(body['start_date'], "%d-%m-%Y").date(),
            end_date = datetime.datetime.strptime(body['end_date'], "%d-%m-%Y").date(),
            payment =body['payment'],
            start_time = datetime.datetime.strptime(body['start_time'], '%H:%M').time(),
            end_time = datetime.datetime.strptime(body['end_time'], "%H:%M").time(),
            location = body['location'],
            phone_number = body['phone_number'],
            employer = user
        )
        job.save()
    except:
        return JsonResponse({'error': 'There was an error creating the job, please try again!'})
    return JsonResponse({'error': ''})    



def get_all_jobs(request):
    queryset = Job.objects.order_by('-id')
    serializer = JobSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)
