from django.shortcuts import render, redirect

from . import models


def index(request):
    context = {"title": "Todo", "todos": models.Todo.objects.all()}
    return render(request, "core/index.html", context)


def add_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        body = request.POST.get("body")
        models.Todo.objects.create(title=title, body=body)
    return redirect("index")


def delete_todo(request, pk):
    if request.method == "POST":
        models.Todo.objects.get(pk=pk).delete()
    return redirect("index")
