from django.db import models

# Create your models here.


class Persona(models.Model):
    persona_type = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Persona: {self.persona_type}'


# class Brief(models.Model):
#     lead = ForeignKey(Lead, related_name="has_brief")
#     art_info = 
#     message = models.TextField()
#     number_of_works = models.IntegerField()
#     budget_min = models.IntegerField()
#     budget_max = models.IntegerField()
#     images = 

