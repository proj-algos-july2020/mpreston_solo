# Generated by Django 2.2 on 2020-07-10 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quiz', '0001_initial'),
        ('leads', '0002_delete_lead'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email_address', models.CharField(blank=True, max_length=255)),
                ('phone_number', models.CharField(max_length=45)),
                ('budget', models.IntegerField()),
                ('intent_score', models.IntegerField()),
                ('newsletter_opt_out', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('persona_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_leads', to='quiz.Persona')),
            ],
        ),
    ]
