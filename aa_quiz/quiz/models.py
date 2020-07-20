from django.db import models

# Create your models here.


class Persona(models.Model):
    persona_type = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.persona_type}'
