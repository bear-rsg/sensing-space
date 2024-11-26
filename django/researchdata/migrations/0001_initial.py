# Generated by Django 4.2.16 on 2024-11-21 12:29

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('code', models.CharField(blank=True, help_text='Hex code of colour, e.g. FF0000', max_length=255, null=True)),
            ],
            options={
                'ordering': [django.db.models.functions.text.Upper('name')],
            },
        ),
        migrations.CreateModel(
            name='Emotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('emoji', models.CharField(blank=True, help_text='Emoji character that represents this emotion, e.g. 😀', max_length=5, null=True)),
                ('order', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['order', django.db.models.functions.text.Upper('name')],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': [django.db.models.functions.text.Upper('name')],
            },
        ),
        migrations.CreateModel(
            name='TimesExperiencedEffects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('order', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'times experienced effects',
                'ordering': ['order', django.db.models.functions.text.Upper('name')],
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geolocation_latitude', models.CharField(blank=True, max_length=100, null=True)),
                ('geolocation_longitude', models.CharField(blank=True, max_length=100, null=True)),
                ('where_are_you_specific', models.CharField(blank=True, max_length=255, null=True, verbose_name='Type in your location, if not in above list')),
                ('have_you_been_in_this_space_before', models.BooleanField(blank=True, null=True, verbose_name='Have you been in this space before?')),
                ('visual_trigger', models.BooleanField(blank=True, null=True, verbose_name='Is something you can see affecting how you feel?')),
                ('visual_things_i_see_moving', models.BooleanField(blank=True, null=True, verbose_name='Things I can see around me are moving')),
                ('visual_things_i_see_predictable', models.BooleanField(blank=True, null=True, verbose_name='Things I can see around me are predictable')),
                ('visual_this_space_looks_dark', models.BooleanField(blank=True, null=True, verbose_name='This space looks dark')),
                ('visual_this_space_looks_bright', models.BooleanField(blank=True, null=True, verbose_name='This space looks bright')),
                ('visual_this_space_looks_colourful', models.BooleanField(blank=True, null=True, verbose_name='This space looks colourful')),
                ('visual_this_space_looks_highcontrast', models.BooleanField(blank=True, null=True, verbose_name='This space looks high contrast')),
                ('visual_this_space_looks_cluttered', models.BooleanField(blank=True, null=True, verbose_name='This space looks cluttered')),
                ('visual_this_space_looks_empty', models.BooleanField(blank=True, null=True, verbose_name='This space looks empty')),
                ('visual_tell_us_more', models.TextField(blank=True, null=True, verbose_name='Tell us more about how what you see affects your experience')),
                ('visual_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Upload an image of your space')),
                ('audio_trigger', models.BooleanField(blank=True, null=True, verbose_name='Is something you can hear affecting how you feel?')),
                ('audio_i_can_hear_general_background_noise', models.BooleanField(blank=True, null=True, verbose_name='I can hear general background noise')),
                ('audio_i_can_hear_specific_noise', models.BooleanField(blank=True, null=True, verbose_name='I can hear specific noises')),
                ('audio_i_can_hear_intermittent_noise', models.BooleanField(blank=True, null=True, verbose_name='I can hear intermittent noise')),
                ('audio_tell_us_more', models.TextField(blank=True, null=True, verbose_name='Tell us more about how what you hear affects your experience')),
                ('audio_file', models.FileField(blank=True, null=True, upload_to='', verbose_name='Upload an audio recording of your space')),
                ('body_trigger', models.BooleanField(blank=True, null=True, verbose_name='Is the environment around you affecting how you feel? ')),
                ('body_can_you_move_comfortably', models.BooleanField(blank=True, null=True, verbose_name='Can you move through the space comfortably?')),
                ('body_do_you_have_enough_space', models.BooleanField(blank=True, null=True, verbose_name='Do you have enough space around you?')),
                ('body_is_there_air_moving', models.BooleanField(blank=True, null=True, verbose_name='Is there a breeze or air moving?')),
                ('body_tell_us_more', models.TextField(blank=True, null=True, verbose_name='Tell us more about how your physical environment affects your experience')),
                ('smell', models.BooleanField(blank=True, null=True, verbose_name='Is there a noticeable smell in this space?')),
                ('smell_tell_us_more', models.TextField(blank=True, null=True, verbose_name='Tell us more about how what you smell affects your experience')),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='unique key')),
                ('audio_i_can_hear_general_background_noise_emotion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='survey_audio_i_can_hear_general_background_noise_emotion', to='researchdata.emotion', verbose_name='I can hear general background noise - how does this affect you?')),
                ('audio_i_can_hear_intermittent_noise_emotion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='survey_audio_i_can_hear_intermittent_noise_emotion', to='researchdata.emotion', verbose_name='I can hear intermittent noise - how does this affect you?')),
                ('audio_i_can_hear_specific_noise_emotion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='survey_audio_i_can_hear_specific_noise_emotion', to='researchdata.emotion', verbose_name='I can hear specific noises - how does this affect you?')),
                ('body_can_you_move_comfortably_emotion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='survey_body_can_you_move_comfortably_emotion', to='researchdata.emotion', verbose_name='Can you move through the space comfortably? - how does this affect you?')),
                ('body_do_you_have_enough_space_emotion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='survey_body_do_you_have_enough_space_emotion', to='researchdata.emotion', verbose_name='Do you have enough space around you? - how does this affect you?')),
                ('body_is_there_air_moving_emotion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='survey_body_is_there_air_moving_emotion', to='researchdata.emotion', verbose_name='Is there a breeze or air moving? - how does this affect you?')),
                ('final_colour_represent_mood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='survey', to='researchdata.colour', verbose_name='Pick a colour that represents your mood')),
                ('final_times_experienced_effects', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='survey', to='researchdata.timesexperiencedeffects', verbose_name='How many times have you experienced these effects before in this space?')),
                ('how_is_your_day_going_emotion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='survey_how_is_your_day_going_emotion', to='researchdata.emotion', verbose_name='How is your day going so far?')),
                ('smell_emotion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='survey_emotion', to='researchdata.emotion', verbose_name='Is there a noticeable smell in this space? - how does this affect you?')),
                ('visual_things_i_see_moving_emotion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='survey_visual_things_i_see_moving_emotion', to='researchdata.emotion', verbose_name='Things I can see around me are moving - how does this affect you?')),
                ('visual_things_i_see_predictable_emotion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='survey_visual_things_i_see_predictable_emotion', to='researchdata.emotion', verbose_name='Things I can see around me are predictable - how does this affect you?')),
                ('visual_this_space_looks_bright_emotion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='survey_visual_this_space_looks_bright_emotion', to='researchdata.emotion', verbose_name='This space looks bright - how does this affect you?')),
                ('visual_this_space_looks_cluttered_emotion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='survey_visual_this_space_looks_cluttered_emotion', to='researchdata.emotion', verbose_name='This space looks cluttered - how does this affect you?')),
                ('visual_this_space_looks_colourful_emotion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='survey_visual_this_space_looks_colourful_emotion', to='researchdata.emotion', verbose_name='This space looks colourful - how does this affect you?')),
                ('visual_this_space_looks_dark_emotion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='survey_visual_this_space_looks_dark_emotion', to='researchdata.emotion', verbose_name='This space looks dark - how does this affect you?')),
                ('visual_this_space_looks_empty_emotion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='survey_visual_this_space_looks_empty_emotion', to='researchdata.emotion', verbose_name='This space looks empty - how does this affect you?')),
                ('visual_this_space_looks_highcontrast_emotion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='survey_visual_this_space_looks_higtcontrast_emotion', to='researchdata.emotion', verbose_name='This space looks high contrast - how does this affect you?')),
                ('where_are_you', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='survey', to='researchdata.location', verbose_name='Where are you?')),
            ],
        ),
    ]