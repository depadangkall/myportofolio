from django.forms import ModelForm, NumberInput, Select, Textarea, TextInput

from main.models import Education, Experience


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
