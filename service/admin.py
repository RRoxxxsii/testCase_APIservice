from django.contrib import admin

from service.models import Employee, Store, Visit


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ('user_name',)


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    search_fields = ('store__user__user_name', 'store__name')
