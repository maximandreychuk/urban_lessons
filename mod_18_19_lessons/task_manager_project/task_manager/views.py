import datetime
import random
from .forms import ContactForm
from django.shortcuts import redirect, render
from .models import Comment, Page, Task


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


# далее - Домашнее задание по теме "DTL. Подробнее о шаблонах и тегах.
def array(request):
    lst = []
    comments = Comment.objects.all()
    for c in comments:
        lst.append(c)
    return render(request, 'arrays.html', {'comments': lst})


def different_time_formats(request):
    dt = datetime.datetime.now()
    return render(request, 'different_time_formats.html', {'dt': dt})


def get_all_pages(request):
    pages = Page.objects.all()
    return render(request, 'all_pages.html', {'pages': pages})


def get_page_detail(request, page_slug):
    page = Page.objects.get(slug=page_slug)
    return render(request, 'page_detail.html', {'page': page})


def random_tag_color(request):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return render(request, 'random_color_template.html', {'r': r, 'g': g, 'b': b})
