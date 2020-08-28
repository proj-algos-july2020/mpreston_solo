from django.db import models

# Create your models here.


class Persona(models.Model):
    # PERSONA_TYPE_CHOICES = [
    #     ('LIVING_WELL', 'Living Well'),
    #     ('HIP_ENTHUSIAST', 'Hip Enthusiast'),
    #     ('COLLECTOR', 'Collector'),
    #     ('UNKNOWN', 'Unknown')
    # ]
    # persona_type = models.CharField(
    #     max_length=45,
    #     choices=PERSONA_TYPE_CHOICES,
    #     default='UNKNOWN',
    #     )
    persona_type = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # related name = 'has_leads'
    # related name = 'has_actions'

    def __str__(self):
        return f'{self.persona_type}'


class Action(models.Model):
    action = models.CharField(max_length=45)
    description = models.TextField()
    for_persona = models.ManyToManyField(Persona, related_name="has_actions", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
