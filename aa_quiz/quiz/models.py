from django.db import models

# Create your models here.


class Persona(models.Model):
    persona_type = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'< Persona object: {self.persona_type} ({self.id})>'


# class LivingWellCouple(models.Model):
#     # LIVING_WELL_COUPLE = 'LW'
#     # HIP_ENTHUSIAST = 'HE'
#     # COLLECTOR = 'CO'
#     # DABBLER = 'DB'
#     # PERSONA_TYPE_CHOICES = [
#     #     (LIVING_WELL_COUPLE, 'Living Well Couple'),
#     #     (HIP_ENTHUSIAST, 'Hip Enthusiast'),
#     #     (COLLECTOR, 'Collector'),
#     #     (DABBLER, 'Dabbler'),
#     # ]
    
#     # persona_type = models.CharField(max_length=2, choices=PERSONA_TYPE_CHOICES)

# class PersonaQuestion(models.Model):
#     persona_type = ForeignKey(Persona, related_name="has_questions", on_delete=models.CASCADE)
#     question = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class IntentQuestion(models.Model):
#     intent_score = models.IntegerField()
#     question = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Brief(models.Model):
#     lead = ForeignKey(Lead, related_name="has_brief")
#     persona_score = # an array of persona codes assigned as persona questions are answered
#     intent_score = # a sum of intent scores given as intent questions are answered
#     message = models.TextField()
#     number_of_works = models.IntegerField()
#     budget = models.IntegerField()
#     photos

