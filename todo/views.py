from django.shortcuts import render
from todo.models import Todo

def todo(request):

    if request.method == 'POST':
        todo_id = request.POST['todo_id']      
        # todo_status = request.POST['todo_status']
        
        # print(todo_id)
        todo = Todo.objects.get(id=todo_id)
        # print(todo)
        if todo.status == True:
            todo.status = False 
            todo.save()                      
        else:
            todo.status = True  
            todo.save()          

    todolists = Todo.objects.all().order_by('-task_added_at')
    context = {
        'todolists':todolists,
    }

    return render(request, 'todo/todo.html', context)