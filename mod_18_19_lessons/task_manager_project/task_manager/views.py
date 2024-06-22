from .forms import ContactForm
from django.shortcuts import redirect, render
from .models import Task, Comment


def get_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


def get_task(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'task_detail.html', {'task': task})


def get_five_comments(request):
    five_comments = Comment.objects.all().order_by('-id')[:5]
    return render(request, 'latest_messages.html', {'comments': five_comments})


def get_user_info(request):
    return render(request, 'user_info.html', {'user': request.user})


def add_comment(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        cf = ContactForm(request.POST or None)
        if cf.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(
                task=task, user=request.user, content=content)
            comment.save()
            return redirect(task.get_absolute_url())
        else:
            cf = ContactForm()
        return render(request, 'add_comment.html', {'comment_form': cf})
