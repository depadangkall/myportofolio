from django.urls import path

from main.views import (
    create_experience,
    delete_experience,
    get_experience_json,
    show_education,
    show_experience,
    show_main,
    show_moments,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("education/", show_education, name="show_education"),
    path("moments/", show_moments, name="show_moments"),
]
