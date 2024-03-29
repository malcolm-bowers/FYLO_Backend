"""
Definition of models.
"""

from re import T
from django.db import models
from django.urls import reverse

# Create your models here.

class Base(models.Model):
    name = models.CharField(max_length=200, help_text='Enter the base.')

    location = models.CharField(max_length=200, help_text='Enter the state for this base.')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('base-detail', args=[str(self.id)])

class Command(models.Model):
    name = models.CharField(max_length=200, help_text='Enter an Army Command (e.g. TRADOC)')

    def __str__(self):
        """Strting for representing the Model object."""
        return self.name

class Brigade(models.Model):
    """Model representing a Brigade"""
    name = models.CharField(max_length=200, help_text='Enter the Brigade.')
    
    command = models.ForeignKey(Command, on_delete=models.RESTRICT, null=True)

    base = models.ManyToManyField(Base, null=True, help_text='Select a base for this Brigade.')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this Brigade."""
        return reverse('brigade-detail', args=[str(self.id)])

class Battalion(models.Model):
    name = models.CharField(max_length=200, help_text='Enter the Battalion.')

    brigade = models.ForeignKey(Brigade, on_delete=models.RESTRICT, null=True)

    base = models.ManyToManyField(Base, help_text='Select a base for this Battalion.')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this Battalion."""
        return reverse('battalion-detail', args=[str(self.id)])

class Company(models.Model):
    name = models.CharField(max_length=200, help_text='Enter the Company.')

    battalion = models.ForeignKey(Battalion, on_delete=models.RESTRICT, null=True)

    base = models.ManyToManyField(Base, help_text='Select a base for this Battalion.')

    def __str__(self):
        """String for representing the Model object."""
        return (self.name + ", " + self.battalion.name)

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this Company."""
        return reverse('company-detail', args=[str(self.id)])

def generate_filename():
    pass

class File(models.Model):
    name = models.CharField(max_length=200, help_text='Enter the file name.')
    file = models.FileField(upload_to="files/%Y/%m%d")
    base = models.ForeignKey(Base, on_delete=models.CASCADE, null=True, blank=True)
    command = models.ForeignKey(Command, on_delete=models.CASCADE, null=True, blank=True)
    brigade = models.ForeignKey(Brigade, on_delete=models.CASCADE, null=True, blank=True)
    battalion = models.ForeignKey(Battalion, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name