from django.db import models


class AbstractBaseModel(models.Model):
    """AbstractBaseModel contains common fields between models.

    All models should extend this class.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Department(AbstractBaseModel):
    """Department represents the sector a set of employees belongs to."""

    dept_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, unique=True)
    supervisor_name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Employee(AbstractBaseModel):
    """Employee represents the people from a given department."""

    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, db_index=True)
    email = models.EmailField(unique=True)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_join = models.DateField(verbose_name='Date Join')
    active=models.BooleanField(verbose_name='active', default=True)

    def __str__(self):
        return self.name

class Apprisal(AbstractBaseModel):
    """Apprisal of the employees."""

    apprisal_id = models.AutoField(primary_key=True, unique=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    overall_ratings = models.TextField()

    def __str__(self):
        return self.apprisal_id


    