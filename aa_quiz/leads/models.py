from django.db import models
from quiz.models import Persona
import re

# Create your models here.

class LeadManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['contact-first-name']) < 2:
            errors['fname'] = "First name must be at least 2 characters."
        if len(postData['contact-last-name']) < 2:
            errors['lname'] = "Last name must be at least 2 characters."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['contact-email']):
            errors['email'] = "Please enter a valid email address"
        if int(postData['contact-budget-min']) < 500:
            errors['min_budget'] = "We require a minimum budget of $500 for this service."
        if int(postData['contact-budget-max']) < int(postData['contact-budget-min']):
            errors['max_budget'] = "Max budget must be greater than min budget."
        return errors


class Lead(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=45, blank=True)
    budget_min = models.IntegerField()
    budget_max = models.IntegerField()
    intent_score = models.IntegerField()
    persona_type = models.ForeignKey(Persona, related_name="has_leads", on_delete=models.CASCADE)
    images = models.ImageField(null=True, upload_to='lead_uploads')
    quiz_brief = models.TextField()
    newsletter_opt_in = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = LeadManager()

    def __str__(self):
        return f'Lead: {self.first_name} {self.last_name}'