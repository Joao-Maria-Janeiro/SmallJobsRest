from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    employer = serializers.ReadOnlyField(source='employer.first_name', read_only=True)
    employee = serializers.ReadOnlyField(source='employee.first_name', read_only=True)
    class Meta:
        model = Job
        fields = ('id','title', 'description', 'start_date', 'end_date', 'payment', 'start_time',
            'end_time', 'location', 'phone_number', 'employer', 'employee')






