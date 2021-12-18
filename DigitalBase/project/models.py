from django.db import models
from django.core.validators import MaxValueValidator

class Project(models.Model):
    name = models.CharField(
        max_length = 120
    )
    job_number = models.PositiveBigIntegerField(
        validators = [MaxValueValidator(999999, 'Invalid Job Number')]
    )
    display_name = models.CharField(
        max_length = 120,
        blank = True
    )

    def __str__(self):
        return self.name