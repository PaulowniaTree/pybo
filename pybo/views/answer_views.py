from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import AnswerForm
# Create your views here.
from ..models import Question


@login_required(login_url='common:login')
def answer_create(request, question_id):
    '''
    pybo 답변 등록
    '''
    # question = get_object_or_404(Question, pk=question_id)
    # question.answer_set.create(content=request.POST.get('content'),
    #                            create_date=timezone.now())
    # return redirect('pybo:detail', question_id=question_id)

    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question' : question, 'form':form}
    return render(request, 'pybo/question_detail.html', context)