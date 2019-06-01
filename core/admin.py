from django.contrib import admin
from .models import Project, Action


def regenerate_token(modeladmin, request, queryset):
    queryset.update(token=Project.generate_token())

regenerate_token.short_description = "Regenerate project token"


class ActionAdmin(admin.TabularInline):
    model = Action
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ActionAdmin,
    ]
    filter_horizontal = ('users',)
    search_fields = ['name', 'slug']
    list_display = ['name', 'slug', 'token']
    readonly_fields = ('slug', 'token',)

    actions = [regenerate_token]


admin.site.register(Project, ProjectAdmin)
