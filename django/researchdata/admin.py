from django.contrib import admin
from . import models


@admin.register(models.Colour)
class ColourAdminView(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')
    search_fields = ('id', 'name', 'code')


@admin.register(models.Emotion)
class EmotionAdminView(admin.ModelAdmin):
    list_display = ('id', 'name', 'emoji', 'order')
    search_fields = ('id', 'name', 'emoji', 'order')


@admin.register(models.Location)
class LocationAdminView(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('id', 'name')


@admin.register(models.TimesExperiencedEffects)
class TimesExperiencedEffectsAdminView(admin.ModelAdmin):
    list_display = ('id', 'name', 'order')
    search_fields = ('id', 'name', 'order')


@admin.register(models.Survey)
class SurveyAdminView(admin.ModelAdmin):
    list_display = (
        'id', 'slug', 'location', 'geolocation_latitude',
        'geolocation_longitude', 'geolocation_accuracy', 'created'
    )
    search_fields = ('id', 'slug', 'admin_notes', 'created')
    ordering = ('-created',)
    readonly_fields = ('created', 'slug')
    fieldsets = (
        ('Start', {
            'fields': (
                'geolocation_latitude',
                'geolocation_longitude',
                'geolocation_accuracy',
                'where_are_you',
                'where_are_you_specific',
                'have_you_been_in_this_space_before',
                'how_is_your_day_going_emotion',
            )
        }),
        ('Visual', {
            'fields': (
                'visual_trigger',
                'visual_things_i_see_moving',
                'visual_things_i_see_moving_emotion',
                'visual_things_i_see_predictable',
                'visual_things_i_see_predictable_emotion',
                'visual_this_space_looks_dark',
                'visual_this_space_looks_dark_emotion',
                'visual_this_space_looks_bright',
                'visual_this_space_looks_bright_emotion',
                'visual_this_space_looks_colourful',
                'visual_this_space_looks_colourful_emotion',
                'visual_this_space_looks_highcontrast',
                'visual_this_space_looks_highcontrast_emotion',
                'visual_this_space_looks_cluttered',
                'visual_this_space_looks_cluttered_emotion',
                'visual_this_space_looks_empty',
                'visual_this_space_looks_empty_emotion',
                'visual_tell_us_more',
                'visual_image'
            )
        }),
        ('Audio', {
            'fields': (
                'audio_trigger',
                'audio_i_can_hear_general_background_noise',
                'audio_i_can_hear_general_background_noise_emotion',
                'audio_i_can_hear_specific_noise',
                'audio_i_can_hear_specific_noise_emotion',
                'audio_i_can_hear_intermittent_noise',
                'audio_i_can_hear_intermittent_noise_emotion',
                'audio_tell_us_more',
                'audio_file',
            )
        }),
        ('Body', {
            'fields': (
                'body_trigger',
                'body_can_you_move_comfortably',
                'body_can_you_move_comfortably_emotion',
                'body_do_you_have_enough_space',
                'body_do_you_have_enough_space_emotion',
                'body_is_there_air_moving',
                'body_is_there_air_moving_emotion',
                'body_tell_us_more',
            )
        }),
        ('Smell', {
            'fields': (
                'smell',
                'smell_emotion',
                'smell_tell_us_more',
            )
        }),
        ('Final', {
            'fields': (
                'final_times_experienced_effects',
                'final_colour_represent_mood',
            )
        }),
        ('Other', {
            'fields': (
                'admin_notes',
                'created',
                'slug'
            )
        }),
    )
