from django.contrib import admin
from .models import regFORM

@admin.register(regFORM)
class UserAdmin(admin.ModelAdmin):
    list_display=('name','phoneno','email','dob')
