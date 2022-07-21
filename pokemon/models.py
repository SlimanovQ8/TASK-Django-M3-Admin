from django.db import models

# Create your models here.
class Pokemon(models.Model):
    class PokemonType(models.TextChoices):
        WATER = 'WA', ('WATER')
        GRASS = 'GR', ('GRASS')
        GHOST = 'GH', ('GHOST')
        STEEL = 'ST', ('STEEL')
        FAIRY = 'FA', ('FAIRY')


    name = models.CharField(
        max_length=30
    )
    type = models.CharField(
        max_length=30,
        choices= PokemonType.choices,
        default= PokemonType.WATER,
    )
    hp = models.PositiveIntegerField()
    active = models.BooleanField(
        default=True
    )

    name_fr = models.CharField(max_length=30)
    name_ar = models.CharField(max_length=30)
    name_jp = models.CharField(max_length=30)
    created_at= models.DateTimeField()
    models_at= models.DateTimeField()


