# Generated by Django 2.2 on 2020-07-19 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0007_auto_20200719_2105'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='lead',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='lead',
            old_name='newsletter_opt_out',
            new_name='newsletter_opt_in',
        ),
    ]
