from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "I Gede Devadatta",
        "npm": "2506622481",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Information Systems student at Universitas Indonesia. Into "
            "business, marketing, and whatever geeky thing has my attention. "
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Deva",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)