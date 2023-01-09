from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from .models import Type,Note
from .forms import NoteForm
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

class TypeListView(ListView):
    model = Type
    template_name = "todo/default.html"


class NoteListView(ListView):
    model = Note
    template_name = "todo/List_details.html"

    def get_queryset(self):
        return Note.objects.filter(type_id=self.kwargs["type_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["List_details"] = Type.objects.get(id=self.kwargs["type_id"])
        return context

class TypeCreate(CreateView):
    model = Type
    # template_name = "todo/add_type.html"
    fields = ["title"]

    def get_context_data(self):
        context = super(TypeCreate, self).get_context_data()
        context["title"] = "Add a new type"
        return context

    def get_success_url(self):
        return reverse("default")

class NoteCreate(CreateView):
    model = Note
    form_class= NoteForm

    def get_initial(self):
        initial_data = super(NoteCreate, self).get_initial()
        todo_type = Type.objects.get(id=self.kwargs["type_id"])
        initial_data["List_details"] = todo_type
        return initial_data

    def get_context_data(self):
        context = super().get_context_data()
        todo_type = Type.objects.get(id=self.kwargs["type_id"])
        context["List_details"] = todo_type
        context["title"] = "Create a new note"
        return context

    def get_success_url(self):
        return reverse("type", args=[self.object.type_id])

class NoteUpdate(UpdateView):
    model = Note
    form_class= NoteForm
    def get_context_data(self):
        context = super(NoteUpdate, self).get_context_data()
        context["List_details"] = self.object.type
        context["title"] = "Edit note"
        return context

    def get_success_url(self):
        return reverse("type", args=[self.object.type_id])

class TypeDelete(DeleteView):
    model = Type   
    success_url = reverse_lazy("default")

class NoteDelete(DeleteView):
    model = Note

    def get_success_url(self):
        return reverse_lazy("type", args=[self.kwargs["type_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["List_details"] = self.object.type
        return context