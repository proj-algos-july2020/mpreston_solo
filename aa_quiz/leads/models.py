from django.db import models
from quiz.models import Persona
import re
from PIL import Image


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
            errors['email'] = "Please enter a valid email address."
        if not postData['contact-budget-min']:
            errors['budget-min'] = "Please enter a minimum budget."
        if not postData['contact-budget-max']:
            errors['budget-max'] = "Please enter a maximum budget."
        return errors


class Lead(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=45, blank=True)
    budget_min = models.IntegerField()
    budget_max = models.IntegerField()
    intent_score = models.IntegerField()
    has_persona = models.ManyToManyField(Persona, related_name="has_leads", blank=True)
    uploads = models.ImageField(null=True, upload_to='lead_uploads')
    quiz_brief = models.TextField()
    newsletter_opt_in = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = LeadManager()

    def __str__(self):
        return f'Lead: {self.first_name} {self.last_name}'