# Register your models here.
from django.contrib import admin
from .models import TeamMember, Location, TeamName


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'location', 'team', 'start_date']
    list_filter = ['role']
    search_fields = ['name', 'role', 'team', 'location']
    date_hierarchy = 'start_date'


admin.site.register(TeamMember, TeamMemberAdmin)


class TeamNameAdmin(admin.ModelAdmin):
    list_display = ['team']


admin.site.register(TeamName, TeamNameAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = ['location']


admin.site.register(Location, LocationAdmin)

admin.site.site_header = 'Company Administration'
admin.site.index_title = 'Team Management Administration'
