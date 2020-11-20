from django.shortcuts import render
from .models import ToDo
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):

    ############################ Displaying items from database ########################## 
    todo_items = ToDo.objects.all().order_by("-date_created")
    todo_dict = {"todo_items":todo_items} 
    return render(request, "ToDo_App/index.html", todo_dict)

def add_todo(request):

    ########################## CREATE #######################################
    date_created = timezone.now()
    content = request.POST["content"]
    # print(content)
    ToDo.objects.create(text=content, date_created=date_created)
    length_of_todos = ToDo.objects.all().count()

    return HttpResponseRedirect("/")

def delete_item(request, todo_id):
    # print(todo_id)
    ToDo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
