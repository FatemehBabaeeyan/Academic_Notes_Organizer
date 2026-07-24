from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm
from courses.models import Course
from django.db.models import Q

@login_required
def note_create(request, course_id):
    course = get_object_or_404(Course,id=course_id,user=request.user )
    if request.method == "POST":
        form = NoteForm(request.POST,request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.course = course
            note.save()
            return redirect("course_list")
    else:
        form = NoteForm()
    return render(request,"notes/note_create.html",
        {
            "form": form,
            "course": course,
        }
    )
@login_required
def note_list(request, course_id):
    course = get_object_or_404(Course,id=course_id,user=request.user)
    search = request.GET.get("search")
    notes = course.notes.all()
    if search:
        notes = notes.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search) |
            Q(content__icontains=search)
        )
    return render(request,"notes/note_list.html",
        {
            "course": course,
            "notes": notes,
        }
    )
@login_required
def note_update(request, pk):

    note = get_object_or_404(Note,pk=pk,course__user=request.user)
    if request.method == "POST":
        form = NoteForm(request.POST,request.FILES,instance=note)
        if form.is_valid():
            form.save()
            return redirect(
                "note_list",
                course_id=note.course.id
            )

    else:
        form = NoteForm(instance=note)
    return render(request,"notes/note_update.html",
        {
            "form": form,
            "note": note,
        }
    )
@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note,pk=pk,course__user=request.user )
    if request.method == "POST":
        course_id = note.course.id
        note.delete()
        return redirect("note_list",course_id=course_id)

    return render(request,"notes/note_delete.html",
        {
            "note": note,
        }
    )