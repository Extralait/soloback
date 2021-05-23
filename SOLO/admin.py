from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

# Register your models here.
from SOLO.models import *

admin.site.register(Division)
admin.site.register(Positions)
admin.site.register(Vocation)
admin.site.register(User)
admin.site.register(Interest)


# @admin.register(User)
# class UserAdmin(DjangoUserAdmin):
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('name', 'surname', 'fathers_name')}),
#         ('Permissions', {
#             'fields': ('is_active', 'is_staff', 'is_superuser'),
#         }),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2', 'name', 'surname', 'fathers_name'),
#         }),
#     )
#     list_display = ('email', 'name', 'surname', 'fathers_name')
#     search_fields = ('email', 'name',)
#     ordering = ('email',)
