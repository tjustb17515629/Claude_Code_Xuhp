from datetime import date

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .models import Todo


def list_view(request):
    filter_status = request.GET.get('filter', 'all')
    filter_category = request.GET.get('category', '')

    todos = Todo.objects.all()

    if filter_status == 'active':
        todos = todos.filter(completed=False)
    elif filter_status == 'completed':
        todos = todos.filter(completed=True)

    if filter_category:
        todos = todos.filter(category=filter_category)

    total = Todo.objects.count()
    active = Todo.objects.filter(completed=False).count()
    completed = Todo.objects.filter(completed=True).count()

    return render(request, 'todo/list.html', {
        'todos': todos,
        'total': total,
        'active': active,
        'completed': completed,
        'filter_status': filter_status,
        'filter_category': filter_category,
        'categories': Todo._meta.get_field('category').choices,
        'today': date.today(),
    })


def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        if title:
            Todo.objects.create(
                title=title,
                category=request.POST.get('category', 'study'),
                due_date=request.POST.get('due_date') or None,
                tags=request.POST.get('tags', '').strip(),
            )
            messages.success(request, '任务已添加')
    return redirect('list')


def toggle_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    messages.success(request, '任务已标记为' + ('已完成' if todo.completed else '进行中'))
    return redirect('list')


def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    messages.success(request, '任务已删除')
    return redirect('list')


def edit_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        if title:
            todo.title = title
            todo.category = request.POST.get('category', 'study')
            todo.due_date = request.POST.get('due_date') or None
            todo.tags = request.POST.get('tags', '').strip()
            todo.completed = request.POST.get('completed') == 'on'
            todo.save()
        return redirect('list')

    return render(request, 'todo/edit.html', {
        'todo': todo,
        'categories': Todo._meta.get_field('category').choices,
        'today': date.today(),
    })
