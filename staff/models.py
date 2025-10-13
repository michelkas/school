"""
Modèles pour la gestion du personnel (staff, rôles, doyens, etc.).
Chaque classe et méthode est documentée selon les standards Pylint.
"""

from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse

class Role(models.Model):
    """
    Modèle représentant un rôle attribuable à un membre du staff (ex : enseignant, administrateur).
    """
    name = models.CharField("Role", max_length=100, unique=False, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'role'
        verbose_name = 'role'
        verbose_name_plural = 'roles'
        ordering = ['name']

    def __str__(self):
        """
        Retourne le nom du rôle.
        Returns:
            str: Nom du rôle.
        """
        return self.name

    def formatted_created_at(self):
        """
        Retourne la date de création formatée.
        Returns:
            str: Date formatée.
        """
        return self.created_at.strftime("%Y-%m-%d %H:%M:%S")

    def formatted_updated_at(self):
        """
        Retourne la date de mise à jour formatée.
        Returns:
            str: Date formatée.
        """
        return self.updated_at.strftime("%Y-%m-%d %H:%M:%S")

class Staff(models.Model):
    """
    Modèle représentant un membre du staff (enseignant, administratif, etc.).
    Contient les informations personnelles, professionnelles et de contact.
    """
    SEXE_CHOICE = [
        ('masculin', 'Masculin'),
        ('féminin', 'Feminin')
    ]
    TITLE_CHOICES = [
        ('Mr.', 'Monsieur'),
        ('Mme.', 'Madame'),
        ('Mlle.', 'Mademoiselle'),
        ('Me.', 'Maitre'),
        ('Dr.', 'Docteur'),
        ('Pr.', 'Professeur'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField("Nom", max_length=100, unique=False, null=False, blank=False)
    surname = models.CharField("Post Nom", max_length=100, unique=False, null=False, blank=False)
    firstname = models.CharField("Prenom", max_length=100, unique=False, null=False, blank=False)
    sexe = models.CharField(max_length=10, null=True, choices=SEXE_CHOICE, default="masculin")
    role = models.ManyToManyField(Role, blank=True)
    email = models.EmailField(null=True, blank=True)
    contact = PhoneNumberField("Contact📞", region='CD', null=True, blank=True, unique=True)
    title = models.CharField("Titre", max_length=60, choices=TITLE_CHOICES, blank=True, null=True)
    degree = models.CharField("Niveau d'etude", max_length=100, unique=False, null=True, blank=True)
    faculty = models.CharField("Domaine", max_length=100, unique=False, null=True, blank=True)
    matricule = models.CharField(max_length=100, unique=True, blank=True, editable=False)
    date_birthday = models.DateField("Date de naissance", null=True, blank=True)
    admin = models.BooleanField('Admin', default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'staff'
        verbose_name = 'fonctionnaire'
        verbose_name_plural = 'fonctionnaires'
        ordering = ['name']

    def __str__(self):
        """
        Retourne le nom du staff.
        Returns:
            str: Nom du staff.
        """
        return self.name

    def formatted_created_at(self):
        """
        Retourne la date de création formatée.
        Returns:
            str: Date formatée.
        """
        return self.created_at.strftime("%Y-%m-%d %H:%M:%S")

    def formatted_updated_at(self):
        """
        Retourne la date de mise à jour formatée.
        Returns:
            str: Date formatée.
        """
        return self.updated_at.strftime("%Y-%m-%d %H:%M:%S")

class Dean(models.Model):
    """
    Modèle représentant un doyen (Dean) responsable d'une section et d'une option.
    """
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    section = models.ForeignKey('education.Section', on_delete=models.CASCADE)
    option = models.ForeignKey('education.Options', on_delete=models.CASCADE)
    course = models.ManyToManyField('education.Course', blank=True)
    start_date = models.DateField("Date de nommination", null=False)
    end_date = models.DateField("Date de fin mandat", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Dean'
        verbose_name = 'Titulaire d\'option'
        verbose_name_plural = 'Titulaires d\'options'
        
    def __str__(self):
        return f"{self.staff.name} {self.staff.firstname}"
   
    
    def formatted_created_at(self):
        """
        Retourne la date de création formatée.
        Returns:
            str: Date formatée.
        """
        return self.created_at.strftime("%Y-%m-%d %H:%M:%S") # Format as needed
    
    def formatted_updated_at(self):
        """
        Retourne la date de mise à jour formatée.
        Returns:
            str: Date formatée.
        """
        return self.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    
    def format_start_date(self):
        """
        Retourne la date de début de manière formatée.
        Returns:
            str: Date formatée.
        """
        return self.start_date.strftime("%d-%B-%Y")
     
    def format_end_date(self):
        """
        Retourne la date de fin de manière formatée.
        Returns:
            str: Date formatée ou "-" si pas de date de fin.
        """
        return self.end_date.strftime("%d-%B-%Y") if self.end_date else "-"


