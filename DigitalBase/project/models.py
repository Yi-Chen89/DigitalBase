from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey


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
    description = models.TextField()
    parent_id = ForeignKey(
        "self",
        on_delete = models.CASCADE,
        null = True
    )
    project_id = ForeignKey(
        Project,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.name