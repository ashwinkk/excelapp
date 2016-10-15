from django.contrib import admin
from .models import Events,Department,Rule

# Register your models here.

admin.site.register(Events)
admin.site.register(Department)
admin.site.register(Rule)