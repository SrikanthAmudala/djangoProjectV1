# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Task

# Register your models here.
admin.site.site_header = "TODO Server APP | Admin Dashboard"


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'status', 'taskDueDate', 'userID')
    readonly_fields = ('title', 'status', 'taskDueDate', 'desc')


#     def has_add_permission(self, request):
#         return False
#
#     def has_change_permission(self, request, obj=None):
#         return False
#
#     def has_delete_permission(self, request, obj=None):
#         return False
# #
# @admin.register(Task)
# class MyAdmin(admin.ModelAdmin):
#     readonly_fields = ('title','status','taskDueDate', 'desc')
#     actions = None # Removes the default delete action in list view
#
#     def has_add_permission(self, request):
#         return False
#
#     def has_change_permission(self, request, obj=None):
#         return False
#
#     def has_delete_permission(self, request, obj=None):
#         return False
# admin.site.unregister(User)
# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#
#     pass
admin.site.register(Task, TaskAdmin)
admin.site.unregister(Group)
