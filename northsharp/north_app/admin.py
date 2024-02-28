from django.contrib import admin
from .models import Student,Subject,Grade,Employee,Table


admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(Employee)
admin.site.register(Table)
