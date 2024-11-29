from django.db import migrations, transaction
from .. import models
import random


def insert_data(apps, schema_editor):
    """
    Inserts default data into the database
    e.g. values of select list models
    """

    # Colours
    colours = [
        {'name': 'red', 'code': 'E71934'},
        {'name': 'purple', 'code': 'B00B72'},
        {'name': 'blue', 'code': '1F87E8'},
        {'name': 'pink', 'code': 'F37EF0'},
        {'name': 'green', 'code': '80D71E'},
        {'name': 'yellow', 'code': 'F1E308'},
        {'name': 'orange', 'code': 'F1A508'},
        {'name': 'grey', 'code': 'C1C1C1'},
    ]
    for colour in colours:
        with transaction.atomic():
            models.Colour.objects.create(**colour)

    # Emotions
    emotions = [
        {'name': 'Positive', 'emoji': '😀', 'order': 1},
        {'name': 'Neutral', 'emoji': '😐', 'order': 2},
        {'name': 'Negative', 'emoji': '😞', 'order': 3},
    ]
    for emotion in emotions:
        with transaction.atomic():
            models.Emotion.objects.create(**emotion)

    # TimesExperiencedEffects
    times = [
        {'name': 'Never', 'order': 1},
        {'name': 'Less than 5', 'order': 2},
        {'name': '5-10', 'order': 3},
        {'name': 'More than 10', 'order': 4},
    ]
    for time in times:
        with transaction.atomic():
            models.TimesExperiencedEffects.objects.create(**time)


class Migration(migrations.Migration):

    dependencies = [
        ('researchdata', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_data)
    ]
