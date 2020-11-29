from django.contrib import admin
from .models import *

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id','title')

@admin.register(Yangiliklar)
class YangiliklarAdmin(admin.ModelAdmin):
    list_display = ('id','title','rasm')

@admin.register(Galereya)
class GalereyaAdmin(admin.ModelAdmin):
    list_display = ('id','rasm')