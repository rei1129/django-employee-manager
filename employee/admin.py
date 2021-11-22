from django.contrib import admin
from .models import Club, Department, Employee
# Register your models here.

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Club)
