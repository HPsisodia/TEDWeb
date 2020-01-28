from django.db import models

# Create your models here.

SPONSORS_STATUS = ((1, 'Applied'), (2, 'Reviewing'), (3, 'Accepted'), (4, 'Rejected'))

class SponsorApplicationData(models.Model):
    name = models.Charfield(max_length = 150)
    domain = models.Charfield(max_length = 150)
    POC = models.Charfield(max_length = 150)
    contactNo = models.Charfield(max_length = 11)
    email = models.Charfield(max_length = 100)
    logo = models.ImageField()
    status = models.IntegerField(choices = SPONSORS_STATUS)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

class SponsorData(models.Model):
    name = models.Charfield(max_length = 150)
    domain = models.Charfield(max_length = 150)
    Website = models.URLField(max_length = 256)
    Image = models.ImageField()
    is_previous = models.BooleanField()
    is_deleted = models.BooleanField(default = False)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name
