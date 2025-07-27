from django.shortcuts import render
from django.http import HttpResponse
from . models import Todo_List

# Create your views here.
def todo_home(request):
    if request.method == "POST":
        title = request.POST.get('title')
        update_btn = request.POST.get('update_btn')
        delete_btn = request.POST.get('delete_btn')

        # Add new task
        if title:
            todo = Todo_List(title=title)
            todo.save()

        # Mark task complete
        elif update_btn:
            try:
                task = Todo_List.objects.get(todo_id=int(update_btn))
                task.complete = True
                task.save()
            except Todo_List.DoesNotExist:
                pass

        # Delete task
        elif delete_btn:
            try:
                task = Todo_List.objects.get(todo_id=int(delete_btn))
                task.delete()
            except Todo_List.DoesNotExist:
                pass

    # Always reload list from DB
    todo_list = Todo_List.objects.all()
    return render(request, "Todo_app/todo.html", {"todo_list": todo_list})
