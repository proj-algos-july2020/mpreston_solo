from django.db import models

# Create your models here.


class Persona(models.Model):
    persona_type = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # related name = 'has_leads'
    # related name = 'has_actions'

    def __str__(self):
        return f'{self.persona_type}'

    # def main():
    #     # Instantiate PERSONA TYPES with the following IDs:
    #     # 1 - LIVING WELL
    #     # 2 - HIP ENTHUSIAST
    #     # 3 - COLLECTOR
    #     # 4 - UNKNOWN
    #     p1 = Persona(persona_type='LIVING WELL')
    #     p2 = Persona(persona_type='HIP ENTHUSIAST')
    #     p3 = Persona(persona_type='COLLECTOR')
    #     p4 = Persona(persona_type='UNKNOWN')


class Action(models.Model):
    action = models.CharField(max_length=45)
    description = models.TextField()
    for_persona = models.ManyToManyField(Persona, related_name="has_actions", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
