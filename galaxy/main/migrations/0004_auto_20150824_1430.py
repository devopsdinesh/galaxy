# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

import math


def round_score_up(apps, schema_editor):
    # Going forward each rating will contain a single score from 1 to 5.
    db_alias = schema_editor.connection.alias
    Ratings = apps.get_model("main", "RoleRating")
    for rating in Ratings.objects.using(db_alias).all():
        rating.score = math.ceil(rating.score)
        rating.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150824_1354'),
    ]

    operations = [
        migrations.RunPython(round_score_up),
    ]
