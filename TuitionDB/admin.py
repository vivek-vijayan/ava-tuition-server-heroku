from django.contrib import admin

# Register your models here.

from .models import Student, Leader, A2Portal_access

admin.site.register(Student)
admin.site.register(Leader)
admin.site.register(A2Portal_access)
