from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_todo_app.models import Employer, Companies

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ('id', 'name','designation','salary','joining_date', 'updated_at','supervisor')

class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ('id', 'name','work_type','number_of_employees','founding_date')