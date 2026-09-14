from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Education, Experience, Moment


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
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Ongoing")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "No experience has been added yet.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Finished")
        self.assertNotContains(response, "Ongoing")

    def test_education_url_is_accessible(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")

    def test_education_page(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertContains(response, self.education.institution)
        self.assertContains(response, "Present")

    def test_empty_education_page(self):
        Education.objects.all().delete()
        response = self.client.get(reverse("main:show_education"))

        self.assertContains(response, "No education history has been added yet.")

    def test_completed_education(self):
        self.education.end_year = 2029
        self.education.save()
        response = self.client.get(reverse("main:show_education"))

        self.assertFalse(self.education.is_ongoing)
        self.assertContains(response, "2029")
        self.assertNotContains(response, "Present")

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