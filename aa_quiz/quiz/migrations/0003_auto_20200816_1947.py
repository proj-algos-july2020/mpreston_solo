# Generated by Django 2.2 on 2020-08-16 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='action',
            name='action',
            field=models.CharField(max_length=45),
        ),
    ]
