from django.db import models

"""
field :
    nom officiel, numero d'agrement, code d'identification, province, statut juridique, promo
"""

class Core(models.Model):
    official_name = models.CharField("Nom officiel de l'école", max_length= 255, null=False, blank=False)
    number = models.CharField("Numero d'agrément", max_length= 255, blank=True)
    code = models.CharField("code d'identification de l'école", max_length= 255, blank=True)
    province = models.CharField("Province Educationnelle", max_length= 255, blank=True)
    statut = models.TextField("Statut juridique", blank=True)
    promo = models.CharField("Promoteur de l'école", max_length= 255, blank=True)

    class Meta:
        db_table = 'hero'

    def __str__(self):
        return self.official_name



