from django.contrib import admin

from apps.domains.metadata.models import People


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name_kor', 'name_foreign', 'gender', 'birth_date', 'death_date',)
