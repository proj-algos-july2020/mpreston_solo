# Generated by Django 2.2 on 2020-07-18 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_auto_20200717_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='images',
            field=models.ImageField(null=True, upload_to='lead_uploads'),
        ),
    ]