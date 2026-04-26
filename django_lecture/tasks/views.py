from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    


def index(request):
    # render a template called tasks
    # then provide some context/ information that index.html needs
    # it needs access to all my tasks
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            
            # 1. Pull the data, defaulting to an empty list
            tasks = request.session.get("tasks", [])
            
            # 2. SANITY CHECK: If it's a dict, force it to be a list
            if isinstance(tasks, dict):
                tasks = []
            
            # 3. Now append safely
            tasks.append(task)
            
            # 4. Save it back (this overwrites the old dict with the new list)
            request.session["tasks"] = tasks
            
            return HttpResponseRedirect(reverse("tasks:index")) 
        
    return render(request, "tasks/add.html",{
        "form": NewTaskForm()
        })

    