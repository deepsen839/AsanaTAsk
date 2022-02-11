from django.contrib import admin
from .models import asanaModel
# Register your models here.
@admin.register(asanaModel)
class asanaModelAdmin(admin.ModelAdmin):
    #fields = ('taskname','notes')
    list_display = ('taskname','notes')
