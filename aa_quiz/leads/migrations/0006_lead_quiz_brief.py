# Generated by Django 2.2 on 2020-07-19 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0005_lead_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='quiz_brief',
            field=models.TextField(default=()),
            preserve_default=False,
        ),
    ]
