from rest_framework import viewsets

from staff.models import Department, Employee, Apprisal
from staff.serializers import DepartmentSerializer, EmployeeSerializer, ApprisalSerializer
from rest_framework.permissions import IsAuthenticated


class DepartmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows Departments to be viewed or edited.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_fields = ('dept_id','name', 'supervisor_name')


class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows Employees to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_fields = ('name', 'email', 'dept_id', 'date_join', 'active')

class ApprisalViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows Employees to be viewed or edited.
    """
    queryset = Apprisal.objects.all()
    serializer_class = ApprisalSerializer
    filter_fields = ('apprisal_id', 'employee_id', 'overall_ratings')