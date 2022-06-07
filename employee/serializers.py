from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers

from .models import Employee
from bank.models import Branch

class UserSerializer(Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    mobile_number = serializers.CharField(max_length=11)

class CreateEmployeeSerializer(ModelSerializer):
    employee_id = serializers.IntegerField()
    branch_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Employee
        fields = ('employee_id', 'branch_id')
    
    def create(self, validated_data):
        employee_id = validated_data.get('employee_id')
        branch_id = validated_data.get('branch_id')

        branch = Branch.objects.get(id=branch_id)
        employee = Employee.objects.create(employee_id=employee_id, branch=branch)

        return employee