from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.utils import timezone


def index(request):
    question_list = Question.objects.order_by('-created_datetime')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):
    """
    답변등록
    :param request: content(string)
    :param question_id: int
    :return:
    """
    question = get_object_or_404(Question, pk=question_id)
    # question.answer_set.create(content=request.POST.get('content'), created_datetime=timezone.now())
    answer = Answer(question=question, content=request.POST.get('content'), created_datetime=timezone.now())
    answer.save()
    return redirect('pybo:detail', question_id=question_id)
