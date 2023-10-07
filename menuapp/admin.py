from django.contrib import admin
from .models import MenuItem


class ChildrenInline(admin.TabularInline):
    model = MenuItem
    extra = 1


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'menu_name', 'parent')
    fields = ('title', 'menu_name', 'url', 'parent', 'is_active')
    inlines = (ChildrenInline, )

