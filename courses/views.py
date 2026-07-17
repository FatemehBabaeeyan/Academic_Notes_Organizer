from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from .models import Course
from .forms import CourseForm
from django.shortcuts import get_object_or_404

@login_required
def course_list(request):

    courses = Course.objects.filter(user=request.user)

    return render(
        request,
        "courses/course_list.html",
        {"courses": courses},
    )
@login_required
def course_create(request):

    if request.method == "POST":

        form = CourseForm(request.POST)

        if form.is_valid():

            course = form.save(commit=False)

            course.user = request.user

            course.save()

            return redirect("course_list")

    else:

        form = CourseForm()

    return render(
        request,
        "courses/course_create.html",
        {"form": form},
    )

@login_required
def course_update(request, pk):
    course = get_object_or_404(
        Course,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)

        if form.is_valid():
            form.save()
            return redirect("course_list")

    else:
        form = CourseForm(instance=course)

    return render(
        request,
        "courses/course_update.html",
        {"form": form}
    )
@login_required
def course_delete(request, pk):

    course = get_object_or_404(
        Course,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":
        course.delete()
        return redirect("course_list")

    return render(
        request,
        "courses/course_delete.html",
        {"course": course}
    )