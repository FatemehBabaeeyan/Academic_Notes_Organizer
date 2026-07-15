from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "professor", "user", "created_at")
    search_fields = ("name", "professor")
    list_filter = ("created_at",)