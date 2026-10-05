import datetime
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from main.forms import EducationForm, ExperienceForm, SkillForm
from main.models import Education, Experience, Moment, Skill

def show_main(request):
    last_login = request.COOKIES.get("last_login", "No login session yet / cookie not found")
    context = {
        "name": "Deva",
        "full_name": "I Gede Devadatta",
        "npm": "2506622481",
        "study_program": "Information Systems",
        "bio": (
            "Information Systems student at Universitas Indonesia. Into "
            "business, marketing, and whatever geeky thing has my attention. "
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

def show_experience(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Deva",
        "title_query": title_query,
        "form": ExperienceForm(),
    }
    return render(request, "experience.html", context)


def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.prefetch_related("starred_by").all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    data = []
    for experience in experiences:
        starred_users = experience.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(experience.id),
            "fields": {
                "title": experience.title,
                "description": experience.description,
                "category": experience.get_category_display(),
                "thumbnail": experience.thumbnail,
                "is_ongoing": experience.is_ongoing,
                "star_count": len(starred_users),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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

@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add experiences."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Experience added successfully.", "pk": str(experience.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@login_required(login_url="/login/")
def update_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=experience_id)

    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience updated successfully!")
        return redirect("main:show_experience")

    context = {
        "name": "Deva",
        "form": form,
        "experience": experience,
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
        
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience deleted successfully!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")


def show_education(request):
    institution_query = request.GET.get("institution", "").strip()

    context = {
        "name": "Deva",
        "institution_query": institution_query,
        "form": EducationForm(),
    }
    return render(request, "education.html", context)


def get_education_json(request):
    institution_query = request.GET.get("institution", "").strip()
    educations = Education.objects.order_by("start_year")

    if institution_query:
        educations = educations.filter(institution__icontains=institution_query)

    data = []
    for education in educations:
        data.append({
            "pk": education.id,
            "fields": {
                "institution": education.institution,
                "thumbnail": education.thumbnail,
                "start_year": education.start_year,
                "end_year": education.end_year,
                "is_ongoing": education.is_ongoing,
            }
        })

    return JsonResponse(data, safe=False)


@login_required(login_url="/login/")
def create_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New education added successfully!")
        return redirect("main:show_education")

    context = {
        "name": "Deva",
        "form": form,
    }
    return render(request, "education_form.html", context)


@require_POST
def create_education_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add education."},
            status=403,
        )

    form = EducationForm(request.POST)
    if form.is_valid():
        education = form.save()
        return JsonResponse(
            {"message": "Education added successfully.", "pk": education.id},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)


@login_required(login_url="/login/")
def update_education(request, education_id):
    if not request.user.has_perm("main.change_education"):
        raise PermissionDenied

    education = get_object_or_404(Education, pk=education_id)
    form = EducationForm(request.POST or None, instance=education)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Education updated successfully!")
        return redirect("main:show_education")

    context = {
        "name": "Deva",
        "form": form,
        "education": education,
    }
    return render(request, "education_form.html", context)


@login_required(login_url="/login/")
def delete_education(request, education_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education deleted successfully!")
        return redirect("main:show_education")

    return redirect("main:show_education")


def show_skills(request):
    name_query = request.GET.get("name", "").strip()

    context = {
        "name": "Deva",
        "name_query": name_query,
        "form": SkillForm(),
    }
    return render(request, "skills.html", context)


def get_skills_json(request):
    name_query = request.GET.get("name", "").strip()
    skills = Skill.objects.prefetch_related("starred_by").order_by("category", "-level", "name")

    if name_query:
        skills = skills.filter(name__icontains=name_query)

    data = []
    for skill in skills:
        starred_users = skill.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": skill.id,
            "fields": {
                "name": skill.name,
                "category": skill.category,
                "category_display": skill.get_category_display(),
                "level": skill.level,
                "level_display": skill.get_level_display(),
                "logo": skill.logo,
                "description": skill.description,
                "star_count": len(starred_users),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)


@login_required(login_url="/login/")
def create_skill(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = SkillForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New skill added successfully!")
        return redirect("main:show_skills")

    context = {
        "name": "Deva",
        "form": form,
    }
    return render(request, "skill_form.html", context)


@require_POST
def create_skill_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add skills."},
            status=403,
        )

    form = SkillForm(request.POST)
    if form.is_valid():
        skill = form.save()
        return JsonResponse(
            {"message": "Skill added successfully.", "pk": skill.id},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)


@login_required(login_url="/login/")
def update_skill(request, skill_id):
    if not request.user.has_perm("main.change_skill"):
        raise PermissionDenied

    skill = get_object_or_404(Skill, pk=skill_id)
    form = SkillForm(request.POST or None, instance=skill)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Skill updated successfully!")
        return redirect("main:show_skills")

    context = {
        "name": "Deva",
        "form": form,
        "skill": skill,
    }
    return render(request, "skill_form.html", context)


@login_required(login_url="/login/")
def delete_skill(request, skill_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    skill = get_object_or_404(Skill, pk=skill_id)

    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill deleted successfully!")

    return redirect("main:show_skills")


@login_required(login_url="/login/")
def toggle_skill_star(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)

    if request.method == "POST":
        if request.user in skill.starred_by.all():
            skill.starred_by.remove(request.user)
        else:
            skill.starred_by.add(request.user)

    return redirect("main:show_skills")


def show_moments(request):
    context = {
        "name": "Deva",
        "moment_list": Moment.objects.all(),
    }
    return render(request, "moments.html", context)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect("main:login")

    context = {
        "name": "Deva",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie("last_login", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return response

    context = {
        "name": "Deva",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie("last_login")
    return response

@login_required(login_url="/login/")
def toggle_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")
