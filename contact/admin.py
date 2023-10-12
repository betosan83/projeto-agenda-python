from django.contrib import admin

from contact import models


# Register your models here.


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'last_name', 'phone',
    ordering = 'first_name',
    search_fields = 'first_name',


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
