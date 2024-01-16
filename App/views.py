from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ToDo
from .forms import ToDoForm

# Create your views here.


def index(request):

    item_list = ToDo.objects.order_by('-date')

    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    form = ToDoForm()
    content = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }

    return render(request, "App/index.html", content)


def remove(request, id):
    item = ToDo.objects.get(id=id)
    item.delete()
    messages.info(request, "Item removed.")
    return redirect("index")
