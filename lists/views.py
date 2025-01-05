from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from lists.forms import TodoForm, TodoListForm
from lists.models import Todo, TodoList
from django.utils.timezone import now
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from .models import Todo  # Re
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone





def index(request):
    return render(request, "lists/index.html", {"form": TodoForm()})

def todolist(request, todolist_id):
    todolist = get_object_or_404(TodoList, pk=todolist_id)

    if request.method == "POST":
        return redirect("lists:add_todo", todolist_id=todolist_id)

    # Calculate 'is_expired' for each todo
    todos = todolist.todos.all()
    today = now().date()
    for todo in todos:
        todo.is_expired = todo.limit_date and todo.limit_date < today

    return render(
        request, 
        "lists/todolist.html", 
        {"todolist": todolist, "todos": todos, "form": TodoForm()}
    )


def add_todo(request, todolist_id):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            user = request.user if request.user.is_authenticated else None
            todo = Todo(
                description=form.cleaned_data["description"],
                limit_date=form.cleaned_data.get("limit_date"),
                todolist_id=todolist_id,
                creator=user,
            )
            todo.save()
            return redirect("lists:todolist", todolist_id=todolist_id)
        else:
            todolist = get_object_or_404(TodoList, id=todolist_id)
            return render(
                request,
                "lists/todolist.html",
                {"form": form, "todolist": todolist},
            )
    return redirect("lists:index")




@csrf_exempt
def update_task(request, task_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_description = data.get('description')

        # Validate and update task description (ensure it is within the max length)
        if len(new_description) > 128:
            return JsonResponse({'success': False, 'message': 'Description too long'})

        try:
            todo = Todo.objects.get(id=task_id)
            todo.description = new_description
            todo.save()
            return JsonResponse({'success': True})
        except Todo.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Task not found'})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})

@login_required
def overview(request):
    if request.method == "POST":
        return redirect("lists:add_todolist")
    return render(request, "lists/overview.html", {"form": TodoListForm()})


def new_todolist(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            # create default todolist
            user = request.user if request.user.is_authenticated else None
            todolist = TodoList(creator=user)
            todolist.save()
            todo = Todo(
                description=request.POST["description"],
                todolist_id=todolist.id,
                creator=user,
            )
            todo.save()
            return redirect("lists:todolist", todolist_id=todolist.id)
        else:
            return render(request, "lists/index.html", {"form": form})

    return redirect("lists:index")


def add_todolist(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            user = request.user if request.user.is_authenticated else None
            todolist = TodoList(title=request.POST["title"], creator=user)
            todolist.save()
            return redirect("lists:todolist", todolist_id=todolist.id)
        else:
            return render(request, "lists/overview.html", {"form": form})

    return redirect("lists:index")



@login_required
def delete_todolist(request, todolist_id):
    """Delete a todolist."""
    todolist = get_object_or_404(TodoList, id=todolist_id, creator=request.user)
    todolist.delete()
    return redirect("lists:overview")



def delete_task(request, todo_id):
    if request.method == 'DELETE':
        # Ensure the request is coming from a valid user, optional security
        if not request.user.is_authenticated:
            return HttpResponseForbidden("You do not have permission to delete this task.")
        
        # Get the task object or return 404 if not found
        todo = get_object_or_404(Todo, id=todo_id)

        # Delete the task
        todo.delete()
        return JsonResponse({"message": "Task deleted successfully."}, status=200)

    return JsonResponse({"error": "Invalid request method"}, status=400)


from django.utils import timezone

def your_view(request):
    today = timezone.now().date()  # Get today's date (date object, not datetime)
    context = {
        'todos': todos,
        'today': today,
    }
    return render(request, 'lists/todolist.html', context)
