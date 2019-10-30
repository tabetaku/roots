from django.contrib import admin

from apps.domains.metadata.models import Content, Participation, People, Video


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_kor', 'content_type', 'start_date', 'end_date',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('content', 'title', 'title_kor', 'order', 'broadcast_date', 'viewer_ratings',)


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_kor', 'gender', 'birth_date', 'death_date',)


@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('video', 'people', 'participant_type',)
