from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Education, Experience, Moment, Skill


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Teaching Assistant",
            description="Helping students understand web development.",
            category="part-time",
        )
        self.education = Education.objects.create(
            institution="Universitas Indonesia",
            start_year=2025,
        )
        self.moment = Moment.objects.create(
            image="/static/img/foto-baru.png",
            caption="Welcoming staff",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/nonexistent-page/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Teaching Assistant")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_experience_json(self):
        response = self.client.get(reverse("main:get_experience_json"))
        fields = response.json()[0]["fields"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(fields["title"], self.experience.title)
        self.assertEqual(fields["description"], self.experience.description)
        self.assertEqual(fields["category"], "Part-Time")
        self.assertTrue(fields["is_ongoing"])

    def test_empty_experience_json(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:get_experience_json"))

        self.assertEqual(response.json(), [])

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:get_experience_json"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertFalse(response.json()[0]["fields"]["is_ongoing"])

    def test_education_url_is_accessible(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")

    def test_education_json(self):
        response = self.client.get(reverse("main:get_education_json"))
        fields = response.json()[0]["fields"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(fields["institution"], self.education.institution)
        self.assertTrue(fields["is_ongoing"])

    def test_empty_education_json(self):
        Education.objects.all().delete()
        response = self.client.get(reverse("main:get_education_json"))

        self.assertEqual(response.json(), [])

    def test_completed_education(self):
        self.education.end_year = 2029
        self.education.save()
        response = self.client.get(reverse("main:get_education_json"))
        fields = response.json()[0]["fields"]

        self.assertFalse(self.education.is_ongoing)
        self.assertFalse(fields["is_ongoing"])
        self.assertEqual(fields["end_year"], 2029)

    def test_skills_url_is_accessible(self):
        response = self.client.get(reverse("main:show_skills"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skills.html")

    def test_skills_json(self):
        Skill.objects.create(name="Django", category="hard", level=3)
        Skill.objects.create(name="Public Speaking", category="soft", level=2)
        response = self.client.get(reverse("main:get_skills_json"))
        names = [item["fields"]["name"] for item in response.json()]

        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(names, ["Django", "Public Speaking"])
        self.assertEqual(response.json()[0]["fields"]["star_count"], 0)

    def test_empty_skills_json(self):
        response = self.client.get(reverse("main:get_skills_json"))

        self.assertEqual(response.json(), [])

    def test_moments_url_is_accessible(self):
        response = self.client.get(reverse("main:show_moments"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "moments.html")

    def test_moments_page(self):
        response = self.client.get(reverse("main:show_moments"))

        self.assertContains(response, self.moment.image)

    def test_empty_moments_page(self):
        Moment.objects.all().delete()
        response = self.client.get(reverse("main:show_moments"))

        self.assertContains(response, "No moments have been added yet.")