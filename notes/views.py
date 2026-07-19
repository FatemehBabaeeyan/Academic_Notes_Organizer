from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm
from courses.models import Course


@login_required
def note_create(request, course_id):

    course = get_object_or_404(
        Course,
        id=course_id,
        user=request.user,
    )

    if request.method == "POST":

        form = NoteForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():

            note = form.save(commit=False)

            note.course = course

            note.save()

            return redirect("course_list")

    else:

        form = NoteForm()

    return render(
        request,
        "notes/note_create.html",
        {
            "form": form,
            "course": course,
        },
    )
@login_required
def note_list(request, course_id):

    course = get_object_or_404(Course,id=course_id,user=request.user)
    notes = course.notes.all()
    return render(request,"notes/note_list.html",
        {
            "course": course,
            "notes": notes,
        },
    )