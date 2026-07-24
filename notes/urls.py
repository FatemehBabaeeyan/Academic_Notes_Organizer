from django.urls import path
from . import views

urlpatterns = [
    path("create/<int:course_id>/",views.note_create,name="note_create"),
    path("course/<int:course_id>/",views.note_list,name="note_list"),
    path("update/<int:pk>/", views.note_update,name="note_update"),
    path("delete/<int:pk>/",views.note_delete,name="note_delete"),
]