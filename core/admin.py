from django.contrib import admin
from .models import Project, Action


class ActionAdmin(admin.TabularInline):
    model = Action
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ActionAdmin,
    ]
    filter_horizontal = ('users',)
    search_fields = ['name', 'slug']
    list_display = ['name', 'slug']
    readonly_fields = ('slug',)

admin.site.register(Project, ProjectAdmin)
