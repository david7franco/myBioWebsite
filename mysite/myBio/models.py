from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    summary = models.TextField()
    experience = models.TextField()  # Consider using a JSONField for structured data
    education = models.TextField()  # Consider using a JSONField for structured data
    skills = models.TextField()  # Consider using a JSONField for structured data
    projects = models.TextField()  # Consider using a JSONField for structured data

    def __str__(self):
        return self.name
