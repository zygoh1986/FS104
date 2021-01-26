from rest_framework import serializers

from staff.models import Department, Employee, Apprisal

# COMMON_FIELDS contains fields which may exist on all serializers.
COMMON_FIELDS = ('created_at', 'updated_at')


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Department
        fields = COMMON_FIELDS + ('dept_id','name', 'supervisor_name')


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = COMMON_FIELDS + ('name', 'email', 'dept_id', 'date_join', 'active')


class ApprisalSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Apprisal
        fields = COMMON_FIELDS + ('apprisal_id', 'employee_id', 'overall_ratings')
