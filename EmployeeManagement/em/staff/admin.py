from django.contrib import admin

from staff.models import Department, Employee, Apprisal


class DepartmentAdmin(admin.ModelAdmin):

    # fields to be displayed on search box
    search_fields = ('name',)

    # columns to be displayed on listing view
    list_display = ('dept_id','name', 'created_at', 'updated_at')


class EmployeeAdmin(admin.ModelAdmin):

    # fields to be displayed on search box
    search_fields = ('name', 'email')

    # columns to be displayed on listing view
    list_display = ('name', 'email', 'dept_id', 'date_join', 'active', 'created_at', 'updated_at')

    # replaces the select box by a search field
    raw_id_fields = ('dept_id',)

class ApprisalAdmin(admin.ModelAdmin):

    # # fields to be displayed on search box
    # search_fields = ('name')

    # columns to be displayed on listing view
    list_display = ('apprisal_id', 'employee_id', 'overall_ratings', 'created_at', 'updated_at')

    # replaces the select box by a search field
    raw_id_fields = ('employee_id',)



admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Apprisal, ApprisalAdmin)
