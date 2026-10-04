from django.urls import path

from main.views import (
    create_education,
    create_education_ajax,
    create_experience,
    create_experience_ajax,
    create_skill,
    create_skill_ajax,
    delete_skill,
    get_skills_json,
    show_skills,
    toggle_skill_star,
    update_skill,
    delete_education,
    delete_experience,
    get_education_json,
    get_experience_json,
    show_education,
    show_experience,
    show_main,
    show_moments,
    update_education,
    update_experience,
    login_user,
    logout_user,
    register,
    toggle_star,

)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
    path("experience/<uuid:experience_id>/edit/", update_experience, name="update_experience"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("education/", show_education, name="show_education"),
    path("education/add/", create_education, name="create_education"),
    path("education/add-ajax/", create_education_ajax, name="create_education_ajax"),
    path("education/<int:education_id>/edit/", update_education, name="update_education"),
    path("education/<int:education_id>/delete/", delete_education, name="delete_education"),
    path("api/education/", get_education_json, name="get_education_json"),
    path("moments/", show_moments, name="show_moments"),
    path("skills/", show_skills, name="show_skills"),
    path("skills/add/", create_skill, name="create_skill"),
    path("skills/add-ajax/", create_skill_ajax, name="create_skill_ajax"),
    path("skills/<int:skill_id>/edit/", update_skill, name="update_skill"),
    path("skills/<int:skill_id>/delete/", delete_skill, name="delete_skill"),
    path("skills/<int:skill_id>/star/", toggle_skill_star, name="toggle_skill_star"),
    path("api/skills/", get_skills_json, name="get_skills_json"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("experience/<uuid:experience_id>/star/", toggle_star, name="toggle_star"),


]
