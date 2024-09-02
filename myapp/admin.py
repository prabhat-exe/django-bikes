from django.contrib import admin

from myapp.models import Emp
from myapp.models import Fm
# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display=('id','name','course')

class FmAdmin(admin.ModelAdmin):
    list_display=('id','name','course')

admin.site.register(Emp,EmpAdmin)
admin.site.register(Fm,FmAdmin)

# admin.site.register(Emp)