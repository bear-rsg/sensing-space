from django import forms
from . import models


class SurveyCreateForm(forms.ModelForm):
    """
    Form to create a Survey
    """

    class Meta:
        model = models.Survey
        fields = [
            'where_are_you',
            'where_are_you_specific',
            'have_you_been_in_this_space_before',
            'how_is_your_day_going_emotion',
        ]


class SurveyUpdateForm(forms.ModelForm):
    """
    Form to update a Survey
    """

    class Meta:
        model = models.Survey
        exclude = [
            'geolocation_latitude',
            'geolocation_longitude',
            'geolocation_accuracy',
            'where_are_you',
            'where_are_you_specific',
            'have_you_been_in_this_space_before',
            'how_is_your_day_going_emotion',

            'final_times_experienced_effects',
            'final_colour_represent_mood',

            'admin_notes',
            'created',
            'slug'
        ]


class SurveyFinalForm(forms.ModelForm):
    """
    Form for final section of a Survey
    """

    class Meta:
        model = models.Survey
        fields = [
            'final_times_experienced_effects',
            'final_colour_represent_mood'
        ]
