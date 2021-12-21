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


class Scope(models.Model):
    name = models.CharField(
        max_length = 120
    )
    description = models.TextField(
        blank = True
    )
    parent_scope = models.ForeignKey(
        'self',
        on_delete = models.CASCADE,
        default = None,
        null = True,
        blank = True
    )
    project = models.ForeignKey(
        Project,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.name