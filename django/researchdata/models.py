from django.db import models
from django.urls import reverse
from django.db.models.functions import Upper
import random


class Colour(models.Model):
    """
    A colour used in a Survey to describe participant's mood
    """

    related_name = 'colour'

    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=255, blank=True, null=True, help_text='Hex code of colour, e.g. FF0000')

    def __str__(self):
        return self.name

    class Meta:
        ordering = [Upper('name')]


class Emotion(models.Model):
    """
    An emotion that the user may feel about a something in the Survey
    """

    related_name = 'emotion'

    name = models.CharField(max_length=255, unique=True)
    emoji = models.CharField(
        max_length=5, blank=True, null=True,
        help_text='Emoji character that represents this emotion, e.g. 😀'
    )
    order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', Upper('name')]


class Location(models.Model):
    """
    A location on campus that a Survey is based on
    """

    related_name = 'location'

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = [Upper('name')]


class TimesExperiencedEffects(models.Model):
    """
    The amount of times user has experienced effects before
    """

    related_name = 'effects'

    name = models.CharField(max_length=255, unique=True)
    order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', Upper('name')]
        verbose_name_plural = 'times experienced effects'


class Survey(models.Model):
    """
    A Survey, involving various questions completed by participants
    """

    related_name = 'survey'

    # Location

    geolocation_latitude = models.CharField(max_length=100, blank=True, null=True)
    geolocation_longitude = models.CharField(max_length=100, blank=True, null=True)
    where_are_you = models.ForeignKey(
        Location, blank=True, null=True,
        on_delete=models.RESTRICT, related_name=related_name,
        verbose_name='Where are you?'
    )
    where_are_you_specific = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name='Where exactly in the above space are you?',
        help_text='e.g. floor number, room number, etc.'
    )
    have_you_been_in_this_space_before = models.BooleanField(
        blank=True, null=True,
        verbose_name='Have you been in this space before?'
    )
    how_is_your_day_going_emotion = models.ForeignKey(
        Emotion, on_delete=models.RESTRICT, blank=True, null=True,
        related_name=f'{related_name}_how_is_your_day_going_emotion',
        verbose_name='How is your day going so far?'
    )

    # Visual

    visual_trigger = models.BooleanField(
        blank=True, null=True,
        verbose_name='Is something you can see affecting how you feel?'
    )

    visual_things_i_see_moving = models.BooleanField(
        blank=True, null=True,
        verbose_name='Things I can see around me are moving'
    )
    visual_things_i_see_moving_emotion = models.ForeignKey(
        Emotion, on_delete=models.RESTRICT, blank=True, null=True,
        related_name=f'{related_name}_visual_things_i_see_moving_emotion',
        verbose_name='Things I can see around me are moving - how does this affect you?'
    )

    visual_things_i_see_predictable = models.BooleanField(
        blank=True, null=True,
        verbose_name='Things I can see around me are predictable'
    )
    visual_things_i_see_predictable_emotion = models.ForeignKey(
        Emotion, on_delete=models.RESTRICT, blank=True, null=True,
        related_name=f'{related_name}_visual_things_i_see_predictable_emotion',
        verbose_name='Things I can see around me are predictable - how does this affect you?'
    )

    visual_this_space_looks_dark = models.BooleanField(
        blank=True, null=True,
        verbose_name='This space looks dark'
    )
    visual_this_space_looks_dark_emotion = models.ForeignKey(
        Emotion, on_delete=models.RESTRICT, blank=True, null=True,
        related_name=f'{related_name}_visual_this_space_looks_dark_emotion',
        verbose_name='This space looks dark - how does this affect you?'
    )

    visual_this_space_looks_bright = models.BooleanField(
        blank=True, null=True,
        verbose_name='This space looks bright'
    )
    visual_this_space_looks_bright_emotion = models.ForeignKey(
        Emotion, on_delete=models.RESTRICT, blank=True, null=True,
        related_name=f'{related_name}_visual_this_space_looks_bright_emotion',
        verbose_name='This space looks bright - how does this affect you?'
    )

    visual_this_space_looks_colourful = models.BooleanField(
        blank=True, null=True,
        verbose_name='This space looks colourful'
    )
    visual_this_space_looks_colourful_emotion = models.ForeignKey(
        Emotion, on_delete=models.RESTRICT, blank=True, null=True,
        related_name=f'{related_name}_visual_this_space_looks_colourful_emotion',
        verbose_name='This space looks colourful - how does this affect you?'
    )

    visual_this_space_looks_highcontrast = models.BooleanField(
        blank=True, null=True,
        verbose_name='This space looks high contrast'
    )
    visual_this_space_looks_highcontrast_emotion = models.ForeignKey(
        Emotion, on_delete=models.RESTRICT, blank=True, null=True,
        related_name=f'{related_name}_visual_this_space_looks_higtcontrast_emotion',
        verbose_name='This space looks high contrast - how does this affect you?'
    )

    visual_this_space_looks_cluttered = models.BooleanField(
        blank=True, null=True,
        verbose_name='This space looks cluttered'
    )
    visual_this_space_looks_cluttered_emotion = models.ForeignKey(
        Emotion, on_delete=models.RESTRICT, blank=True, null=True,
        related_name=f'{related_name}_visual_this_space_looks_cluttered_emotion',
        verbose_name='This space looks cluttered - how does this affect you?'
    )

    visual_this_space_looks_empty = models.BooleanField(
        blank=True, null=True,
        verbose_name='This space looks empty'
    )
    visual_this_space_looks_empty_emotion = models.ForeignKey(
        Emotion, on_delete=models.RESTRICT, blank=True, null=True,
        related_name=f'{related_name}_visual_this_space_looks_empty_emotion',
        verbose_name='This space looks empty - how does this affect you?'
    )

    visual_tell_us_more = models.TextField(
        blank=True, null=True,
        verbose_name='Tell us more about how what you see affects your experience'
    )
    visual_image = models.ImageField(
        blank=True, null=True,
        verbose_name='Upload an image of your space'
    )

    # Audio

    audio_trigger = models.BooleanField(
        blank=True, null=True,
        verbose_name='Is something you can hear affecting how you feel?'
    )

    audio_i_can_hear_general_background_noise = models.BooleanField(
        blank=True, null=True,
        verbose_name='I can hear general background noise'
    )
    audio_i_can_hear_general_background_noise_emotion = models.ForeignKey(
        Emotion, on_delete=models.RESTRICT, blank=True, null=True,
        related_name=f'{related_name}_audio_i_can_hear_general_background_noise_emotion',
        verbose_name='I can hear general background noise - how does this affect you?'
    )

    audio_i_can_hear_specific_noise = models.BooleanField(
        blank=True, null=True,
        verbose_name='I can hear specific noises'
    )
    audio_i_can_hear_specific_noise_emotion = models.ForeignKey(
        Emotion, on_delete=models.RESTRICT, blank=True, null=True,
        related_name=f'{related_name}_audio_i_can_hear_specific_noise_emotion',
        verbose_name='I can hear specific noises - how does this affect you?'
    )

    audio_i_can_hear_intermittent_noise = models.BooleanField(
        blank=True, null=True,
        verbose_name='I can hear intermittent noise'
    )
    audio_i_can_hear_intermittent_noise_emotion = models.ForeignKey(
        Emotion, on_delete=models.RESTRICT, blank=True, null=True,
        related_name=f'{related_name}_audio_i_can_hear_intermittent_noise_emotion',
        verbose_name='I can hear intermittent noise - how does this affect you?'
    )

    audio_tell_us_more = models.TextField(
        blank=True, null=True,
        verbose_name='Tell us more about how what you hear affects your experience'
    )
    audio_file = models.FileField(
        blank=True, null=True,
        verbose_name='Upload an audio recording of your space'
    )

    # Bodily Comfort

    body_trigger = models.BooleanField(
        blank=True, null=True,
        verbose_name='Is the environment around you affecting how you feel? '
    )

    body_can_you_move_comfortably = models.BooleanField(
        blank=True, null=True,
        verbose_name='Can you move through the space comfortably?'
    )
    body_can_you_move_comfortably_emotion = models.ForeignKey(
        Emotion, on_delete=models.RESTRICT, blank=True, null=True,
        related_name=f'{related_name}_body_can_you_move_comfortably_emotion',
        verbose_name='Can you move through the space comfortably? - how does this affect you?'
    )

    body_do_you_have_enough_space = models.BooleanField(
        blank=True, null=True,
        verbose_name='Do you have enough space around you?'
    )
    body_do_you_have_enough_space_emotion = models.ForeignKey(
        Emotion, on_delete=models.RESTRICT, blank=True, null=True,
        related_name=f'{related_name}_body_do_you_have_enough_space_emotion',
        verbose_name='Do you have enough space around you? - how does this affect you?'
    )

    body_is_there_air_moving = models.BooleanField(
        blank=True, null=True,
        verbose_name='Is there a breeze or air moving?'
    )
    body_is_there_air_moving_emotion = models.ForeignKey(
        Emotion, on_delete=models.RESTRICT, blank=True, null=True,
        related_name=f'{related_name}_body_is_there_air_moving_emotion',
        verbose_name='Is there a breeze or air moving? - how does this affect you?'
    )

    body_tell_us_more = models.TextField(
        blank=True, null=True,
        verbose_name='Tell us more about how your physical environment affects your experience'
    )

    # Smell

    smell = models.BooleanField(
        blank=True, null=True,
        verbose_name='Is there a noticeable smell in this space?'
    )

    smell_emotion = models.ForeignKey(
        Emotion, on_delete=models.RESTRICT, blank=True, null=True,
        related_name=f'{related_name}_emotion',
        verbose_name='Is there a noticeable smell in this space? - how does this affect you?'
    )

    smell_tell_us_more = models.TextField(
        blank=True, null=True,
        verbose_name='Tell us more about how what you smell affects your experience'
    )

    # Final questions

    final_times_experienced_effects = models.ForeignKey(
        TimesExperiencedEffects, on_delete=models.RESTRICT, blank=True, null=True,
        related_name=related_name,
        verbose_name='How many times have you experienced these effects before in this space?'
    )
    final_colour_represent_mood = models.ForeignKey(
        Colour, on_delete=models.RESTRICT, blank=True, null=True,
        related_name=related_name,
        verbose_name='Pick a colour that represents your mood'
    )

    # Other
    admin_notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=30, verbose_name='unique key')

    @property
    def location(self):
        if self.where_are_you_specific in ['', None]:
            return self.where_are_you
        else:
            return f'{self.where_are_you} - {self.where_are_you_specific}'

    def __str__(self):
        return f"Survey #{self.id} | Created: {str(self.created)[:19]} | Location: {self.location}"

    def get_absolute_url(self):
        return reverse('researchdata:survey-update', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        # Set the slug (aka slug) value automatically on creation
        if not self.slug:
            slug = None
            all_slugs = Survey.objects.all().values_list('slug')
            valid_slug_chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
            while not slug or slug in all_slugs:
                slug = ''.join(random.choice(valid_slug_chars) for _ in range(13))
            self.slug = slug
        super().save(*args, **kwargs)
