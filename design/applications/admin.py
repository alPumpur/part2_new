from django.contrib import admin
from .models import *


@admin.register(AdvUser)
class AdvUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email")


@admin.register(CategoryApplication)
class AdminCategoryApplication(admin.ModelAdmin):
    list_display = ("cat_name",)


@admin.register(Application)
class AdminApplication(admin.ModelAdmin):
    list_display = ("name_app", "category")
