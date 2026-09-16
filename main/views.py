from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import ExperienceForm
from main.models import Education, Experience, Moment


def show_main(request):
    context = {
        "name": "Deva",
        "full_name": "I Gede Devadatta",
        "npm": "2506622481",
        "study_program": "Information Systems",
        "bio": (
            "Information Systems student at Universitas Indonesia. Into "
            "business, marketing, and whatever geeky thing has my attention. "
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    json_response = get_experience_json(request)
    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experience_list = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Deva",
        "experience_list": experience_list,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)


def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")


def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New experience added successfully!")
        return redirect("main:show_experience")

    context = {
        "name": "Deva",
        "form": form,
    }
    return render(request, "experience_form.html", context)


def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience deleted successfully!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")


def show_education(request):
    context = {
        "name": "Deva",
        "education_list": Education.objects.all().order_by("start_year"),
    }
    return render(request, "education.html", context)


def show_moments(request):
    context = {
        "name": "Deva",
        "moment_list": Moment.objects.all(),
    }
    return render(request, "moments.html", context)