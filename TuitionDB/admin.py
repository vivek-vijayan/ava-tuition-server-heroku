from django.contrib import admin

# Register your models here.

from .models import Student, Leader, A2Presence_access, A2Complaint_access

admin.site.register(Student)
admin.site.register(Leader)
admin.site.register(A2Presence_access)
admin.site.register(A2Complaint_access)
