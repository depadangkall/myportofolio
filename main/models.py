# Create your models here.
import uuid
from django.db import models
from django.contrib.auth.models import User

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.CharField(max_length=500, blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    starred_by = models.ManyToManyField(User, related_name="starred_experiences", blank=True)

    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None


class Education(models.Model):
    institution = models.CharField(max_length=255)
    thumbnail = models.CharField(max_length=500, blank=True, null = True)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.institution

    @property
    def is_ongoing(self):
        return self.end_year is None


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("hard", "Hard Skill"),
        ("soft", "Soft Skill"),
    ]

    LEVEL_CHOICES = [
        (1, "Beginner"),
        (2, "Intermediate"),
        (3, "Advanced"),
        (4, "Expert"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="hard")
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES, default=2)
    logo = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    starred_by = models.ManyToManyField(User, related_name="starred_skills", blank=True)

    def __str__(self):
        return self.name

class Moment(models.Model):
    image = models.CharField(max_length=500)
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption or self.image