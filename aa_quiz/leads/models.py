from django.db import models
from quiz.models import Persona

# Create your models here.


class Lead(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=45)
    budget_min = models.IntegerField()
    budget_max = models.IntegerField()
    intent_score = models.IntegerField()
    persona_type = models.ForeignKey(Persona, related_name="has_leads", on_delete=models.CASCADE)
    images = models.ImageField(null=True, upload_to='lead_uploads')
    newsletter_opt_out = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Lead: {self.first_name} {self.last_name}'