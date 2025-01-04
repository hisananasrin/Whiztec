from django.shortcuts import render,redirect,get_object_or_404
from .models import Tasks
from django.http import JsonResponse
from django.urls import reverse



# Create your views here.
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')

        if title and due_date:  # Basic validation
            Tasks.objects.create(title=title, description=description, status=status, due_date=due_date)
            return redirect('tasklist')

    return render(request, 'addtask.html')

def task_list(request):
    tasks = Tasks.objects.all()
    return render(request, 'tasklist.html', {'tasks': tasks})

def task_update(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description', '')
        task.status = request.POST.get('status')
        task.due_date = request.POST.get('due_date')

        if task.title and task.due_date:  # Basic validation
            task.save()
            return redirect('tasklist')

    return render(request, 'addtask.html', {'task': task})

def task_delete(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    task.delete()
    return redirect('tasklist')


# def calendar_view(request):
#     tasks = Tasks.objects.all()
#     events = [
#         {
#             "title": task.title,
#             "start": task.due_date.strftime('%Y-%m-%d'),
#             "url": reverse('task_update', args=[task.id])
#         }
#         for task in tasks
#     ]
#     return JsonResponse(events, safe=False)