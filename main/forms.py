from django.core.exceptions import ValidationError
from django.forms import ModelForm, NumberInput, Select, Textarea, TextInput
from django.utils.html import strip_tags

from main.models import Education, Experience, Skill


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "ended_at",
        ]

        labels = {
            "title": "Title",
            "description": "Description",
            "category": "Category",
            "thumbnail": "Thumbnail URL",
            "ended_at": "End Date",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Software Engineer Intern",
                    "maxlength": 255,
                },
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Tell us about your experience",
                    "rows": 3,
                },
            ),
            "category": Select(),
            "thumbnail": TextInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                },
            ),
        }


    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Experience title cannot contain only HTML tags.")
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "institution",
            "thumbnail",
            "start_year",
            "end_year",
        ]

        labels = {
            "institution": "Institution",
            "thumbnail": "Thumbnail URL",
            "start_year": "Start Year",
            "end_year": "End Year",
        }

        widgets = {
            "institution": TextInput(
                attrs={
                    "placeholder": "Universitas Indonesia",
                    "maxlength": 255,
                },
            ),
            "thumbnail": TextInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                },
            ),
            "start_year": NumberInput(
                attrs={
                    "placeholder": "2022",
                },
            ),
            "end_year": NumberInput(
                attrs={
                    "placeholder": "2026",
                },
            ),
        }

    def clean_institution(self):
        institution = strip_tags(self.cleaned_data["institution"]).strip()
        if not institution:
            raise ValidationError("Institution name cannot contain only HTML tags.")
        return institution


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = [
            "name",
            "category",
            "level",
            "logo",
            "description",
        ]

        labels = {
            "name": "Skill Name",
            "category": "Category",
            "level": "Level",
            "logo": "Logo URL (optional, hard skills only)",
            "description": "Description",
        }

        widgets = {
            "name": TextInput(
                attrs={
                    "placeholder": "Django",
                    "maxlength": 100,
                },
            ),
            "category": Select(),
            "level": Select(),
            "logo": TextInput(
                attrs={
                    "placeholder": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg",
                },
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Where and how you use this skill",
                    "rows": 3,
                },
            ),
        }

    def clean_name(self):
        name = strip_tags(self.cleaned_data["name"]).strip()
        if not name:
            raise ValidationError("Skill name cannot contain only HTML tags.")
        return name

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

    def clean_logo(self):
        return strip_tags(self.cleaned_data["logo"]).strip()

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("category") == "soft":
            cleaned_data["logo"] = ""
        return cleaned_data
