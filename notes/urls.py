from django.urls import path
from . import views

urlpatterns = [
    path("create/<int:course_id>/",views.note_create,name="note_create"),
    path("course/<int:course_id>/",views.note_list,name="note_list"),
]